pipeline {
    agent any 
    stages {
        // We removed the "Get Code" stage because Jenkins does it automatically!
        
        stage('Step 1: Build App') {
            steps {
                // This builds your Docker image
                sh 'docker build -t smart-attendance-img .'
            }
        }
        stage('Step 2: Run App') {
            steps {
                // This stops any old version and starts the new one
                sh 'docker stop attendance-app || true'
                sh 'docker rm attendance-app || true'
                sh 'docker run -d --name attendance-app -p 8082:5000 smart-attendance-img'
            }
        }
    }
}