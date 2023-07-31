# image_batch_shap_explainability_radiomics

## Description

This is an SHAP explainability radiomics tool . 



## Usage

#### Step 1: Data Preparation 

The user has to preapre the data by themselves. 

Below you can see an image of the config file .

![config](https://github.com/chaimeleon-eu/image_batch_shap_explainability_radiomics/assets/54101202/39e1e50e-a3d1-4ccc-91ea-a2503980cf4c)



#### Step 2: Build the docker using below command: 

```
docker build -t shap-exp-tool-img .
```


#### Step 3 : For results you have to check the *test_run* folder in the working directory. Following are the results 

Dependancy Plot 

![dependence_plot_feature_0_interaction_0](https://github.com/chaimeleon-eu/image_batch_shap_explainability_radiomics/assets/54101202/43a81f00-0cab-4aa2-8cb5-c5a4fe68ad11)

Global Summary Plot

![summary_plot png](https://github.com/chaimeleon-eu/image_batch_shap_explainability_radiomics/assets/54101202/6fc70c15-d2c1-40ae-affe-22626a642c36)
