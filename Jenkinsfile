pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                script {
                    def scriptPath = 'script_for_db_and_elastic.py'
                    
                    //сhecking the existence of a file
                    if (!fileExists(scriptPath)) {
                       error("File ${scriptPath} not found.  Pipeline aborted.")
                        return;  
                    }
                    
                    sh 'pwd'
                    
                    //script execution
                    sh "python ${scriptPath}"

                }
            }
        }
    }
}

//checking the existence of a file
boolean fileExists(String filePath) {
  return new File(filePath).exists()
}