* Install AWS Credentials
    * Should be in `~/.aws/credentials`
    * Ping Ethan if you have none.

* Clone this Repo!
  * `git clone https://github.com/ejj/quilt-sys-seminar.git`
  * `cd quilt-sys-seminar`

* Edit main.spec
    * Change this line `(define Namespace "CHANGE_ME")`
        * Only necessary if you're on a sharing an aws account

    * Change this line `(githubKey "<YOUR_GITHUB_USERNAME>")`
        * You'll use your github ssh key to log into VMs
        * Alternatively can use `sshkey` with a public ssh key

* Start Quilt!
    * `QUILT_PATH="." ./quilt main.spec`
    * Wait several minutes until you see the "New connection" statement
    * Log into `quilt@<masterIP>`
    * Run `swarm ps` to see currently running containers

* When you're done stop the VMs you started
    * `quilt stop <NAMESPACE>`
    * Wait for "Successfully halted machines."
