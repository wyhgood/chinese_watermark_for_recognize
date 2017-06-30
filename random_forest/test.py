print(__doc__)

# Author: Jan Hendrik Metzen <jhm@informatik.uni-bremen.de>
# License: BSD Style.

import os
import numpy as np
np.random.seed(0)

import matplotlib.pyplot as plt
import time
from PIL import Image
from skimage.feature import hog
from skimage import data, color, exposure
from sklearn import datasets
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC
from sklearn.calibration import calibration_curve

#X, y = datasets.make_classification(n_samples=100000, n_features=20,
#                                    n_informative=2, n_redundant=2)
#print(X.shape)
#print(y.shape)


X = []
y = []


a = np.arange(3200)
print(a.shape)

for path, _, files in os.walk('./result_resize/'):
    print(path)
    i = 0
    for f in files:
        i+=1
        print(f)
        if i>890: break
        im = Image.open(path+f)
        tmp = np.asarray(im)
        image = color.rgb2gray(tmp)
        
        fd, hog_image = hog(image, orientations=9, pixels_per_cell=(16, 16),
                    cells_per_block=(3, 3), visualise=True)

        #X.append(hog_image.reshape((3200)))
        a = np.append(a, hog_image.reshape((3200)))

        
b = np.arange(3200)
for path, _, files in os.walk('./pic_with_word_resize/'):
    print(path)
    i = 0
    for f in files:
        i+=1
        print(f)
        if i>890: break
        im = Image.open(path+f)
        tmp = np.asarray(im)
        image = color.rgb2gray(tmp)

        fd, hog_image = hog(image, orientations=9, pixels_per_cell=(16, 16),
                    cells_per_block=(3, 3), visualise=True)

        #X.append(hog_image.reshape((3200)))                                                                                      
        b = np.append(b, hog_image.reshape((3200)))

X_positive = b.reshape(int(b.shape[0]/3200), 3200)[1:]        
X_negative = a.reshape(int(a.shape[0]/3200), 3200)[1:]
print(X_negative.shape)
print(X_positive.shape)



# X为 训练集32*100的向量集合

train_samples = 800  # Samples used for training the models

X_train = np.append(X_positive[:train_samples], X_negative[:train_samples]).reshape(1600, 3200)
X_test = np.append(X_positive[train_samples:], X_negative[train_samples:]).reshape(180, 3200)
X_positive_test = X_positive[train_samples:]
y_train = np.append(np.zeros(800, dtype='uint8')+1, np.zeros(800, dtype='uint8')).reshape(1600, 1)
y_test = np.append(np.zeros(90, dtype='uint8')+1, np.zeros(90, dtype='uint8')).reshape(180, 1)
#y_train = y[:train_samples]
y_positive_test = np.zeros(90, dtype='uint8')+1
#y_test = y[train_samples:]

print(y_train.shape)
print(X_train.shape)

# Create classifiers
lr = LogisticRegression()
gnb = GaussianNB()
svc = LinearSVC(C=1.0)
rfc = RandomForestClassifier(n_estimators=10)

plt.figure(figsize=(10, 10))
ax1 = plt.subplot2grid((3, 1), (0, 0), rowspan=2)
ax2 = plt.subplot2grid((3, 1), (2, 0))

ax1.plot([0, 1], [0, 1], "k:", label="Perfectly calibrated")
for clf, name in [(lr, 'Logistic'),
                  (gnb, 'Naive Bayes'),
                  (svc, 'Support Vector Classification'),
                  (rfc, 'Random Forest')]:
    clf.fit(X_train, y_train)
    if hasattr(clf, "predict_proba"):
        prob_pos = clf.predict_proba(X_test)[:, 1]
    else:  # use decision function
        prob_pos = clf.decision_function(X_test)
        prob_pos = \
            (prob_pos - prob_pos.min()) / (prob_pos.max() - prob_pos.min())
    fraction_of_positives, mean_predicted_value = \
        calibration_curve(y_test, prob_pos, n_bins=10)

    print(prob_pos.shape)
    print(fraction_of_positives)
    r = clf.score(X_positive_test, y_positive_test)
    print(name)
    print(r)
    print(name)

    ax1.plot(mean_predicted_value, fraction_of_positives, "s-",
             label="%s" % (name, ))

    ax2.hist(prob_pos, range=(0, 1), bins=10, label=name,
             histtype="step", lw=2)

ax1.set_ylabel("Fraction of positives")
ax1.set_ylim([-0.05, 1.05])
ax1.legend(loc="lower right")
ax1.set_title('Calibration plots  (reliability curve)')

ax2.set_xlabel("Mean predicted value")
ax2.set_ylabel("Count")
ax2.legend(loc="upper center", ncol=2)

plt.tight_layout()
plt.show()
