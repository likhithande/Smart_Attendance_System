pipeline {
    agent any 
    stages {
        stage('Step 1: Get Code') {
            steps {
                // This tells Jenkins to pull your latest code from GitHub
                git 'https://github.com/likhithande/Smart_Attendance_System.git'
            }
        }
        stage('Step 2: Build App') {
            steps {
                // This tells Jenkins to build your Docker image
                sh 'docker build -t smart-attendance-img .'
            }
        }
        stage('Step 3: Run App') {
            steps {
                // This stops any old version and starts the new one on port 8082
                sh 'docker stop attendance-app || true'
                sh 'docker rm attendance-app || true'
                sh 'docker run -d --name attendance-app -p 8082:5000 smart-attendance-img'
            }
        }
    }
}