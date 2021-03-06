# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 14:07:18 2019

@author: catcry
"""

""" Implementing A Random Forest on NSL-KDD """


#==============================================================================
#================================   Random Forest   ===========================
#==============================================================================





Xtrain_svm = Xtrain.reshape((len(Xtrain),41))
Xvalid_svm = Xvalid.reshape((len(Xvalid),41))
Xtest_svm  = Xtest.reshape((len(Xtest),41))
Xtest_21_svm = Xtest_21.reshape((len(Xtest_21),41))

#no_estimators = np.array([60])
no_estimators = np.array([1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,90,100,200])
every_repeat_no = 1
no_estimators = np.repeat(no_estimators,every_repeat_no) 

crtron = 'gini'#'entropy' # 'gini' #

maximum_depth = None
min_samp_sp= 2
min_samp_lf = 1
min_weight = 0.0
max_feat = None
max_lf_nodes = None
min_impurity_dec = 0.0
min_impurity_sp = 0.0
bootstrp = True
oob_scor = True
no_jobs = -1
random_st = None
verbs = 0
warm_startt = True
class_wght = None
#------------------------------------------------------------------------------

ac_train_rf = np.zeros(len(no_estimators))
ac_valid_rf = np.zeros(len(no_estimators))
ac_test_rf = np.zeros(len(no_estimators))
ac_test_21_rf  = np.zeros(len(no_estimators))

s_time = np.zeros(len(no_estimators))
e_time = np.zeros(len(no_estimators))

pred_s_time =  np.zeros(len(no_estimators))
pred_e_time =  np.zeros(len(no_estimators))

#------------------------------------------------------------------------------

i=0 
while i<len(no_estimators):


    s_time[i]  = time.time()
   
    clsf = RandomForestClassifier(n_estimators = no_estimators[i] , \
                                  criterion = crtron , \
                                  max_depth = maximum_depth , \
                                  min_samples_split = min_samp_sp , \
                                  min_samples_leaf = min_samp_lf , \
                                  min_weight_fraction_leaf = min_weight , \
                                  max_features = max_feat , \
                                  max_leaf_nodes = max_lf_nodes , \
                                  min_impurity_decrease = min_impurity_dec , \
                                  min_impurity_split = min_impurity_sp , \
                                  bootstrap = bootstrp , \
                                  oob_score = oob_scor , \
                                  n_jobs = no_jobs , \
                                  random_state = random_st , \
                                  verbose = verbs , \
                                  warm_start = warm_startt , \
                                  class_weight = class_wght)
    
    clsf.fit(Xtrain_svm, Ytrain) 
    e_time[i] = time.time()
    
    pred_s_time[i] = time.time()
    
    yh_train_rf = clsf.predict(Xtrain_svm)
    ac_train_rf[i] = accuracy_score(Ytrain,yh_train_rf)
    
    yh_valid_rf = clsf.predict(Xvalid_svm)
    ac_valid_rf[i] = accuracy_score(Yvalid,yh_valid_rf)
    
    
    yh_test_rf = clsf.predict(Xtest_svm)
    ac_test_rf[i] = accuracy_score(Ytest,yh_test_rf)
    
    yh_test_21_rf = clsf.predict(Xtest_21_svm)
    ac_test_21_rf[i] = accuracy_score(Ytest_21,yh_test_21_rf)
    
    pred_e_time[i] = time.time()
    
    



    print('========================================================================')
    print("Results for Random Forest:")
    print('------------------------------------------------------------------------')
    print ('TrainSet Acc = ',round(ac_train_rf[i]*100,3),'%')
    print('')
    print('-----------------------')
    print ('ValidSet Acc = ',round(ac_valid_rf[i]*100,3),'%')
    print('')
    print('-----------------------')
    print('TestSet Acc = ',round(ac_test_rf[i]*100,3),'%')
    print('')
    print('-----------------------')
    print('Test-21 Set Acc = ',round(ac_test_21_rf[i]*100,3),'%')
    print('')
    #print('-----------------------')
    #print('Hard Test Set Acc = ',round(ac_hard_test*100,3),'%')
    #print('')
    print('--------------------------------------------------------------------')
    print('Learning Time = ', round((e_time[i] - s_time[i]),3),'sec')
    print('Prediction on Sets Time = ', round((pred_e_time[i] - pred_s_time[i]),3),'sec')
    print('')
    print('-------------------->    i = ', i, '    <---------------------')
    print('------------------------------------------------------------------------')
    
#    if ac_test_21_rf[i]>0.63:
#        i= len(no_estimators)
    
    i+=1    





