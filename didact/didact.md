<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
  html,
  div,
  body {
    background-color: #1a1a1a;
    font-family: 'IBM Plex Sans', sans-serif;
    font-size: 18px;
    outline: none;
  }
  body {
    font-family: Helvetica, sans-serif;
  }
  /* The actual timeline (the vertical ruler) */
  .timeline {
    position: absolute;
    max-width: 1200px;
    margin: 0 auto;
    margin-left: 50px;
  }
  .content p {
    margin: 0px;
  }
  .content .afterbutton
  {
    padding-top: 16px;
  }
  /* The actual timeline (the vertical ruler) */
  .timeline::after {
    content: '';
    position: absolute;
    width: 1px;
    background-color: white;
    top: 15px;
    bottom: 80px;
    left: 18px;
    margin-left: -2px;
  }
  /* Container around content */
  .container {
    padding: 0px 0px;
    width: 70%;
    align-content: left;
    margin: 0px 0px 0px 0px;
    margin-left: 25px;
    margin-top: 32px;
  }
  /* The circles on the timeline */
  .container::after {
    content: '';
    position: absolute;
    width: 10px;
    height: 10px;
    right: -6px;
    background-color: white;
    border: 0px solid #FF9F55;
    top: 15px;
    border-radius: 50%;
    z-index: 1;
    margin: 0px 0px 0px 0px;
  }
  /* Place the container to the left */
  .left {
    left: 0px;
  }
  /* Place the container to the right */
  .right {
    left: 0px;
  }
  /* Add arrows to the left container (pointing right) */
  .left::before {
    content: " ";
    height: 0;
    top: 22px;
    width: 0;
    z-index: 1;
    right: 30px;
    border: medium solid white;
    border-width: 10px 0 10px 10px;
    border-color: transparent transparent transparent white;
  }
  /* Fix the circle for containers on the right side */
  .right::after {
    left: -13px;
  }
  /* The actual content */
  .content {
    padding: 5px 10px;
    color: white;
    background: transparent;
  }
  .button.is-dark.is-medium {
    font-family: 'IBM Plex Sans', sans-serif;
    background: transparent;
    border-color: white;
    color: #fff;
    border: 1px solid white;
    padding: 10px;
    padding-left: 20px;
    margin-bottom: 13px;
    border-radius: 0px;
    min-width: 180px;
    font-size: 14px;
    text-align: left;
    min-height: 48px;
    margin: 0px;
    justify-content:left;
  }
  .button.is-dark.is-medium:hover {
    font-family: 'IBM Plex Sans', sans-serif;
    background-color: #2a67f5;
    border-color: white;
    color: #fff;
  }
  .footer {
    display: flex;
    background-color: #343A3E;
    margin: 100px 0px 0px 20px;
    padding: 0px;
    max-width: 1200px;
  }
  .github-icon {
    min-height: 100%;
    min-width: 100%;
    object-fit: cover;
    object-position: 250% 100px;
    opacity: 15%;
    bottom: 15px;
  }
  .image-content {
    padding: 5px 10px;
    background: transparent;
    color: black;
    position: absolute;
    font-size: 27px;
  }
  .image-div {
    position: relative;
    background-color: white;
    min-width: 50%;
    background-image: linear-gradient(rgba(255,255,255,0.9), rgba(255,255,255,0.9)), url("https://github.com/bodarajeshkumar/Developer-Playground/blob/master/didact/images/git.svg?raw=true");
    background-position: -50% 60px;
    background-repeat: no-repeat;
    padding-top: 20px;
    padding-left: 20px;
  }
  .image-btn {
    position: absolute;
    right: 0;
    bottom: 0%;
    background-color: #0062FF;
    max-width: 300px;
    min-width: 100px;
    width: 300px;
    padding: 0px;
    padding-bottom: 20px;
  }
  .image-link span
  {
    float: right;
    font-size: 32px;
    padding-right: 10px;
  }
  .image-btn .image-link:hover
  {
    text-decoration: none;
    color: white;
    background-color: #0353E9;
  }
  .image-btn  a:hover
  {
    text-decoration: none;
    color: white;
  }
  .image-link {
    color: white;
    display: block;
    padding: 5px 10px 5px 10px;
    line-height: 28px;
    font-size: 16px;
  }
  .header
  {
    background-image: url('https://s3.us.cloud-object-storage.appdomain.cloud/developer/default/patterns/create-a-web-based-intelligent-bank-loan-application-for-a-loan-agent/header.jpg');
    width: 100%;
    height: fixed;
    min-height: 300px;
    display: inline-block;
    margin-top: 20px;
    margin-bottom: 20px;
    margin-left: 30px;
    margin-right: 30px;
    background-size: contain;
    max-width: 1200px;
    background-size: cover;
  }
  .header .right-content
  {
    float: right;
    width: 45%;
    background-color:#2a67f5;
    min-height:400px;
    padding:20px;
    font-size: 14px;
  }
  .header .right-content h4
  {
    background: none;
    color: white;
    padding-left: 25px;
    padding-right: 25px;
  }
  .header .right-content div
  {
    background: none;
    color: white;
    padding-left: 25px;
    padding-right: 25px;
    font-size: 14px;
    margin-bottom: 10px;
  }
  .header .right-content ul
  {
    margin: 0px;
    margin-left: 25px;
    margin-bottom: 10px;
    line-height: 16px;
  }
  .container a
  {
    color: #78A9FF;
    background-color: transparent;
    text-decoration: none;
  }
  .container a:visited
  {
    color: #8C43FC;
    background-color: transparent;
    text-decoration: none;
  }
  .apptitle
  {
    margin-left: 25px;
    margin-top: 20px;
    margin-bottom: 0px;
    font-size: 25px;
    color: white;
  }
  @media only screen and (max-width: 800px) {
    .footer {
      margin: 950px 0px 0px 20px;
    }
  }
  @media only screen and (max-width: 700px) {
    .footer {
      margin: 1050px 0px 0px 20px;
    }
  }
  @media only screen and (max-width: 600px) {
    .footer {
      margin: 1050px 0px 0px 20px;
    }
  }
  @media only screen and (max-width: 500px) {
    .footer {
      margin: 1100px 0px 0px 20px;
    }
  }
  @media only screen and (max-width: 400px) {
    .footer {
      margin: 1200px 0px 0px 20px;
    }
  }
}
</style>
</head>
  <body>
    <div class="apptitle">
      Cloud pak Loan Agent for IBM® Developer Playground
    </div>
    <div class="header">
      <div class="right-content">
        <div>
            This sample application internally makes REST API calls to the model deployed using Watson Machine Learning.
        </div>
        <div>
            This will show you how Watson Studio instances on Cloud Pak for Data can be used to build a model that would predict the risk involved with a loan application.
        </div>
        <div>
            It also covers how this risk model can be deployed using Watson Machine Learning instances on Cloud Pak for Data.
        </div>
      </div>
    </div>
    <div class="timeline">
      <div class="container right" style="margin-top:0px;padding-top:0px;">
        <div class="content">
          <p>To begin, we'll need to clone the GitHub repository</p>
          <a class="button is-dark is-medium" title="Clone the Repo" href="didact://?commandId=extension.sendToTerminal&text=LoanAgent%7Cget-code%7CLoanAgent|git%20clone%20https://github.com/nupurnegi/cpd-intelligent-loan-agent-app.git;cd%20cpd-intelligent-loan-agent-app">Get Code</a>
        </div>
      </div>
      <div class="container right">
        <div class="content">
          <p>Create and Configure IBM Services</p>
          <p>You need to be logged in to your IBM Cloud account in the Developer Playground to create and configure services.</p>
          <a class="button is-dark is-medium" title="Login to IBM Cloud" href="didact://?commandId=extension.sendToTerminal&text=LoanAgent%7Clogin-ibmcloud%7CLoanAgent|ibmcloud%20login%20--sso%20%26%26%20ibmcloud%20target%20--cf%20%26%26%20ibmcloud%20target%20-g%20Default">Login to IBM Cloud</a>
          <p style="margin-top:10px;">Do not have an IBM Cloud Account?<a href="https://cloud.ibm.com/registration">click here</a> to create one for free.</p>
        </div>
      </div>
      <div class="container right">
        <div class="content">
          <p>This sample application uses the following IBM Services:</p>
          <p><a href="https://cloud.ibm.com/objectstorage">Cloud Object Storage</a>: IBM Cloud Object Storage is a highly scalable cloud storage service, designed for high durability, resiliency and security.</p>
          <p><a href="https://cloud.ibm.com/catalog/services/machine-learning">Watson Machine Learning</a>: Deploy, manage and integrate machine learning models into your applications and services in as little as one click.</p>
          <p><a href="https://cloud.ibm.com/catalog/services/watson-studio">Watson Studio</a>: Develop sophisticated machine learning models using Notebooks and code-free tools to infuse AI throughout your business.</p>
        </div>
      </div>
      <div class="container right">
        <div class="content">
          <p>Create these services and configure the credentials in the code pattern with just a click of button.</p>
          <a class="button is-dark is-medium" title="Create IBM Watson Services" href="didact://?commandId=extension.sendToTerminal&text=LoanAgent%7Ccreate-ibm-services%7CLoanAgent|chmod%20%2Bx%20.%2Fcreate-ibm-cloud-services.sh%20%26%26%20.%2Fcreate-ibm-cloud-services.sh">Create IBM Watson Services</a>
        </div>
      </div>
      <div class="container right">
        <div class="content">
          <p>Go to <a href="https://dataplatform.cloud.ibm.com/">IBM CloudPak for data</a> and login with your IBM id. </p> Once you login follow the below steps to create a new deployment space. You’ll use this space later when you deploy a machine learning model.
          <p>Step 1 : Go to the hamburger (☰) menu and click Deployment > View all spaces as shown in the figure below.</p>
          <img src = "https://raw.githubusercontent.com/nupurnegi/cpd-intelligent-loan-agent-app/master/didact/images/LoanAgent_4.png" width = "750" height= "750">
          <p>Step 2 : Next click on <b>New deployment space +</b> button as shown in the figure below.</p>
          <img src = "https://raw.githubusercontent.com/nupurnegi/cpd-intelligent-loan-agent-app/master/didact/images/LoanAgent_5.png" width = "750" height= "750">
          <p>Step 3 : Create an empty space by selecting <b>Create an empty space</b>.</p>
          <img src = "https://raw.githubusercontent.com/nupurnegi/cpd-intelligent-loan-agent-app/master/didact/images/LoanAgent_6.png" width = "750" height= "750">
          <p>Step 4 : Give your deployment space a unique name and click <b>Create</b>.</p>
          <img src = "https://raw.githubusercontent.com/nupurnegi/cpd-intelligent-loan-agent-app/master/didact/images/LoanAgent_7.png" width = "750" height= "750">
        </div>
      </div>
      <div class="container right">
        <div class="content">
          <p>Next create a new project by following the below steps.</b>
          <p>Step 1 : Go to the hamburger (☰) menu and click Projects > View all projects as shown in the figure below.</p>
          <img src = "https://raw.githubusercontent.com/nupurnegi/cpd-intelligent-loan-agent-app/master/didact/images/LoanAgent_0.png" width = "750" height= "750">
          <p>Step 2 : Next click on <b>New project +</b> button as shown in the figure below.</p>
          <img src = "https://raw.githubusercontent.com/nupurnegi/cpd-intelligent-loan-agent-app/master/didact/images/LoanAgent_1.png" width = "750" height= "750">
          <p>Step 3 : Create an empty project by selecting <b>Create an Empty Project</b>.</p>
          <img src = "https://raw.githubusercontent.com/nupurnegi/cpd-intelligent-loan-agent-app/master/didact/images/LoanAgent_2.png" width = "750" height= "750">
          <p>Step 4 : Name the project, and click <b>Create</b>.</p>
          <img src = "https://raw.githubusercontent.com/nupurnegi/cpd-intelligent-loan-agent-app/master/didact/images/LoanAgent_3.png" width = "750" height= "750">
          <p>Now load the data set to your project. For the data set, you’ll use the <a href="https://s3.us.cloud-object-storage.appdomain.cloud/developer/default/tutorials/infuse-a-loan-department-platform-with-ai/static/german_credit_data.csv"> German credit risk</a> data set.
          <p>Step 5 : From the project overview page, click <b>Add to project +</b> to launch the <b>Choose asset type</b> window.</p>
          <img src = "https://raw.githubusercontent.com/nupurnegi/cpd-intelligent-loan-agent-app/master/didact/images/LoanAgent_8.png" width = "750" height= "750">
          <p>Step 6 : Select <b>Data</b> from the options.</p>
          <img src = "https://raw.githubusercontent.com/nupurnegi/cpd-intelligent-loan-agent-app/master/didact/images/LoanAgent_9.png" width = "750" height= "750">
          <p>Step 7 : Browse for the .csv file and upload it.</p>
          <img src = "https://raw.githubusercontent.com/nupurnegi/cpd-intelligent-loan-agent-app/master/didact/images/LoanAgent_10.png" width = "750" height= "750">
          <p>For the Jupyter notebook, use the <a href="https://s3.us.cloud-object-storage.appdomain.cloud/developer/default/tutorials/infuse-a-loan-department-platform-with-ai/static/machinelearning-creditrisk-sparkmlmodel.ipynb">machinelearning-creditrisk-sparkmlmodel.ipynb</a></p>
          <p>So, similarly upload the Jupyter notebook using <b>Add to project +</b>.</p>
          <p>Step 8 : Select Notebook from the options.</p>
          <img src = "https://raw.githubusercontent.com/nupurnegi/cpd-intelligent-loan-agent-app/master/didact/images/LoanAgent_11.png" width = "750" height= "750">
          <p>Step 9 : Switch to the <b>From file</b> tab. Select runtime <b>Default Python 3.8 XS (2 vCPU 8 GB RAM)</b> </p>
          <p>Next, click <b>Drag and drop files here or upload</b>, upload the machinelearning-creditrisk-sparkmlmodel notebook and click <b>Create</b> to load the Jupyter Notebook.</p>
          <img src = "https://raw.githubusercontent.com/nupurnegi/cpd-intelligent-loan-agent-app/master/didact/images/LoanAgent_12.png" width = "750" height= "750">
        </div>
      </div>
      <div class="container right">
        <div class="content">
            <p>To deploy the ML model to deployment space the program will require API key</p>
            <p>Haven't logged in to IBM Cloud ? then click  <a  href="didact://?commandId=extension.sendToTerminal&text=LoanAgent%7Clogin-ibmcloud%7CLoanAgent|ibmcloud%20login%20-r%20eu-gb%20--sso%20%26%26%20ibmcloud%20target%20--cf%20%26%26%20ibmcloud%20target%20-g%20Default">login to ibm cloud</a></p>
            <p>Click the below button to generate api key through IBM cloud CLI commands.</p><br>
            <a class="button is-dark is-medium" title="Generate API key" href="didact://?commandId=extension.sendToTerminal&text=LoanAgent%7Cgenerate-api-token%7CLoanAgent|cd%20${CHE_PROJECTS_ROOT}/cpd-intelligent-loan-agent-app;ibmcloud%20iam%20api-key-create%20ApiKey-loanAgent%20-d%20'this is API key for loanAgent'%20--file%20${CHE_PROJECTS_ROOT}/cpd-intelligent-loan-agent-app/key_file">Generate api key</a><br> 
        </div>
      </div>
      <div class="container right">
        <div class="content">
          <p>Run the notebook</p>
          <p>Step 1 : Firstly, we have to create project token for the notebook. From the settings tab click <b>New Token +</b></p>
          <img src = "https://raw.githubusercontent.com/nupurnegi/cpd-intelligent-loan-agent-app/master/didact/images/LoanAgent_13.png" width = "750" height= "750">
          <p>Step 2 : Give the project token a name and access role as <b>Editor</b></p>
          <img src = "https://raw.githubusercontent.com/nupurnegi/cpd-intelligent-loan-agent-app/master/didact/images/LoanAgent_14.png" width = "750" height= "750">
          <p>Step 3 : Goto the notebook and click on <b>Insert project token</b> as shown in the below image.</p>
          <img src = "https://raw.githubusercontent.com/nupurnegi/cpd-intelligent-loan-agent-app/master/didact/images/LoanAgent_15.png" width = "750" height= "750">
          <p>Step 4 : Next we have to insert the dataset to the notebook.</p>
          <p>Place cursor below the fifth cell and insert the dataset from toolbar as given below.</p>
          <img src = "https://raw.githubusercontent.com/nupurnegi/cpd-intelligent-loan-agent-app/master/didact/images/LoanAgent_16.png" width = "750" height= "750">
          <p>Step 5 : Copy the variable generated in the previous cell and assign it to the df variable.</p>
          <img src = "https://raw.githubusercontent.com/nupurnegi/cpd-intelligent-loan-agent-app/master/didact/images/LoanAgent_17.png" width = "750" height= "750">
          <p>Step 6 : Follow the comments to fill details in the below two cells.</p>
          <img src = "https://raw.githubusercontent.com/nupurnegi/cpd-intelligent-loan-agent-app/master/didact/images/LoanAgent_19.png" width = "750" height= "750">
          <p>Step 7 : Continue to run all the cells to save the model to IBM Cloud Pak for Data.</p>
        </div>
      </div>
      <div class="container right">
        <div class="content">
          <p>Copy the <b>MODEL_URL</b> generated</p>
          <p>And paste it in .env file.</p>
           <a class="button is-dark is-medium" title="Open File" href="didact://?commandId=extension.openFile&text=LoanAgent%7Cconfigure-application%7C${CHE_PROJECTS_ROOT}/cpd-intelligent-loan-agent-app/.env">Open File</a>
        </div>
      </div>
      <div class="container right">
        <div class="content">
          <p>Install requirements</p>
          <a class="button is-dark is-medium" title="Install requirements" href="didact://?commandId=extension.sendToTerminal&text=LoanAgent%7Cinstall-requirements%7CLoanAgent|cd%20cpd-intelligent-loan-agent-app;pip%20install%20-r%20requirements.txt">Install requirements</a>
        </div>
      </div>
      <div class="container right">
        <div class="content">
          <p>Start the Application</p>
          <a class="button is-dark is-medium" title="Start App" href="didact://?commandId=extension.sendToTerminal&text=LoanAgent%7Cstart-app%7CLoanAgent|python%20app.py">Start App</a>
        </div>
      </div>
    <div class="footer">
      <div class="content" style="padding:30px;padding-left:60px;padding-bottom: 0px;">
        <p>If you'd like to make changes and explore the application, make sure to stop it first!</p>
        <a class="button is-dark is-medium" title="Stop Running Application" href="didact://?commandId=vscode.didact.sendNamedTerminalCtrlC&text=LoanAgent">Stop Running Application</a>
        <p style="margin-top:10px;"> Completed the code pattern? Click on
          <bold>Clean up</bold> to delete the IBM Cloud services that were created.
        </p>
        <a class="button is-dark is-medium" title="Delete services from IBM Cloud" href="didact://?commandId=extension.sendToTerminal&text=LoanAgent%7Cget-code%7CLoanAgent|chmod%20%2Bx%20.%2Fdeleteservice.sh%20%26%26%20.%2Fdeleteservice.sh">Clean up</a>
        <p style="margin-top:10px;">You can also manage the services in
          <a href="https://cloud.ibm.com/resources">IBM Cloud Dashboard</a>.
        </p>
      </div>
      <div class="image-div">
        <p class="image-content">Want to explore this project more?
          <span style="font-size:15px;margin-top:0px;display:block;">Head over to the
            <a href="https://github.com/IBM/cpd-intelligent-loan-agent-app">Github Repository</a>
          </span>
        </p>
        <a class="image-link" href="https://developer.ibm.com/patterns/create-a-web-based-intelligent-bank-loan-application-for-a-loan-agent/" target="_blank">
          <div class="image-btn">
            <p class="image-link">View Product Details</p>
            <p class="image-link"></p>
            <p class="image-link">
              <span>
                <svg style="position: absolute; right: 10px;" fill="#ffffff" focusable="false" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/  svg" width="25" height="25" viewBox="0 0 32 32" aria-hidden="true">
                <path d="M18 6L16.6 7.4 24.1 15 3 15 3 17 24.1 17 16.6 24.6 18 26 28 16z"></path>
                <title>Arrow right</title>
              </svg>
              </span>
            </p>
          </div>
        </a>
      </div>
    </div>
  </body>
</html>
