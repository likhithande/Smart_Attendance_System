pipeline {
    agent any 
    stages {
        stage('Step 1: Build Image') {
            steps {
                // Build with your Docker Hub tag format: username/repository:tag
                sh 'docker build -t andelikhith/smart-attendance-system:latest .'
            }
        }

        stage('Step 2: Login & Push') {
            steps {
                // Replace 'docker-hub-credentials' with the ID you create in Step 3 below
                withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', passwordVariable: 'DOCKER_PASS', usernameVariable: 'DOCKER_USER')]) {
                    sh "docker login -u ${DOCKER_USER} -p ${DOCKER_PASS}"
                    sh 'docker build -t likhithande/smart_attendance_system:latest .'
                }
            }
        }

        stage('Step 3: Deploy Locally') {
            steps {
                sh 'docker stop attendance-app || true'
                sh 'docker rm attendance-app || true'
                sh 'docker run -d --name attendance-app -p 8082:5000 andelikhith/smart-attendance-system:latest'
            }
        }
    }
}