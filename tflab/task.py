import tensorflow as tf

tf.app.flags.DEFINE_string("job_name",
                           "worker",
                           "ps or worker")
tf.app.flags.DEFINE_integer("task_index",
                            0,
                            "task index within a job")
tf.app.flags.DEFINE_string("ps_hosts",
                           "localhost:50001",
                           "ps list like 'localhost:50001,localhost:50002'")
tf.app.flags.DEFINE_string("worker_hosts",
                           "localhost:60001,localhost:60002",
                           "worker list like 'localhost:60001,localhost:60002'")
FLAGS = tf.app.flags.FLAGS

def main(_):
    ps_hosts = FLAGS.ps_hosts.split(',')
    worker_hosts = FLAGS.worker_hosts.split(',')
    cluster = tf.train.ClusterSpec({
        "ps": ps_hosts,
        "worker": worker_hosts})
    server = tf.train.Server(cluster,
                             job_name=FLAGS.job_name,
                             task_index=FLAGS.task_index)
    server.join()

if __name__ == "__main__":
    tf.app.run()
