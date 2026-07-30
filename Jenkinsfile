pipeline {
    agent any
    environment {
        DOCKERHUB_USER = 'manikandanb062005'
        BACKEND_IMAGE  = "${DOCKERHUB_USER}/resume-backend:latest"
        FRONTEND_IMAGE = "${DOCKERHUB_USER}/resume-frontend:latest"
    }
    stages {
        stage('Pull Latest Images') {
            steps {
                sh "docker pull ${BACKEND_IMAGE}"
                sh "docker pull ${FRONTEND_IMAGE}"
            }
        }
        stage('Load Images into kind') {
            steps {
                sh "kind load docker-image ${BACKEND_IMAGE} --name resume-screening"
                sh "kind load docker-image ${FRONTEND_IMAGE} --name resume-screening"
            }
        }
        stage('Approval') {
            steps {
                input message: 'Deploy this build to the local cluster?', ok: 'Deploy'
            }
        }
        stage('Deploy via Helm') {
            steps {
                sh "kubectl rollout restart deployment backend"
                sh "kubectl rollout restart deployment frontend"
                sh "kubectl rollout status deployment backend"
                sh "kubectl rollout status deployment frontend"
            }
        }
        stage('Verify') {
            steps {
                sh "kubectl get pods"
            }
        }
    }
}
