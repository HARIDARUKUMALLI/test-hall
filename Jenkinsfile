def workspace;
node
{
    stage('checkout')
    {
        checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: 'a47187b5-c98f-4228-bd96-718e013741bd', url: 'https://github.com/HARIDARUKUMALLI/SampleProject.git']]])
        workspace =pwd()
    }
    stage('Static code Analysis')
    {
        echo "Static code Analysis"
    }
    stage('build')
    {
        echo "Build the code"
    }
    stage('Unit Testing')
    {
        echo "Unit Testing"
    }
    stage('Delivery')
    {
        echo "Deliver the code"
    }
}