#Execute One
class GitHub:
    def __init__(self,repo_name,request_type,message=None):
        self.repo_name = repo_name
        self.request_type = request_type
        self.message = message
    
    def __str__(self):
        return f"A {self.request_type} request for {self.repo_name} with message {self.message}"
    
    def __call__(self,repo_name,request_type,message=None):
        self.repo_name = repo_name
        self.request_type = request_type
        self.message = message

terraform = GitHub("Terraform","pull")
gitlab = GitHub("GitLab","push","CI Yml files updated")

print(terraform)
print(gitlab)
print("******************************")
terraform("Terraform","push","TF Files updated")
print(terraform)