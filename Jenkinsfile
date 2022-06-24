#!/usr/bin/env groovy

pipeline {
    agent any
    parameters {
        string(name: 'CLIENT_NAME')
        string(name: 'mail_id_of_client')
    }
    stages {
        stage('name_parameter') {
            steps {
                echo "Hello ${CLIENT_NAME}"
                echo "Hello ${mail_id_of_client}"
            }
        }
        
        stage('running-playbook') {
            steps {
                sh 'ansible-playbook ~/workspace/$JOB_NAME/site.yml -e "username="${CLIENT_NAME}"" -e "mail="${mail_id_of_client}"" --vault-password-file "pass.yml"'
            }
        }
    }
}
