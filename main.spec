(import "etcd")
(import "redis")
(import "spark")
(import "zookeeper")

// Etcd Cluster with 3 members.
(etcd.New "etcd" 3)

// Redis cluster with two nodes.
(redis.New "redis" 2 "default_password")

// Spark two masters 3 workers. zookeeper for Spark leader election
(let ((zoo (zookeeper.New "zookeeper" 3))
      (sprk (spark.New "spark" 1 2 zoo)))
  (spark.Job sprk "run-example SparkPi"))

// ============================= Infrastructure ===============================

// Using unique Namespaces will allow multiple Quilt instances to run on the
// same cloud provider account without conflict.
(define Namespace "CHANGE_ME")

// Defines the set of addresses that are allowed to access Quilt VMs.
(define AdminACL (list "local"))

(let ((cfg (list (provider "Amazon")
                 (cpu 2) (ram 8)
                 (githubKey "<YOUR_GITHUB_USERNAME>"))))
  (makeList 1 (machine (role "Master") cfg))
  (makeList 3 (machine (role "Worker") cfg)))
