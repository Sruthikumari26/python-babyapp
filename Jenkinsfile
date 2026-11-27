node {
  stage('SCM') {
    checkout scm
  }
  stage('SonarQube Analysis') {
    def scannerHome = tool 'mysonar';
    withSonarQubeEnv('mysonar) {
      sh "${scannerHome}/bin/sonar-scanner"
    }
  }
}
