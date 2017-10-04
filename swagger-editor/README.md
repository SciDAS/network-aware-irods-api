## Swagger Editor

For the purposes of this project the Swagger Editor will be run locally using Docker.

Github: [swagger-editor](https://github.com/swagger-api/swagger-editor)

### Invoking the Editor

Assumptions

- You are running on a platform where Docker is installed
- You are using an account that has rights to run Docker

From the `swagger-editor/` directory:

```
./run-editor.sh
```

Example:

```
$ ./run-editor.sh
Cloning into 'swagger-editor'...
remote: Counting objects: 31796, done.
remote: Compressing objects: 100% (30/30), done.
remote: Total 31796 (delta 9), reused 17 (delta 5), pack-reused 31761
Receiving objects: 100% (31796/31796), 126.37 MiB | 5.62 MiB/s, done.
Resolving deltas: 100% (17788/17788), done.
Sending build context to Docker daemon  137.8MB
Step 1/11 : FROM alpine:3.4
3.4: Pulling from library/alpine
90f4dba627d6: Pull complete
Digest: sha256:833ad81ace8277324f3ca8c91c02bdcf1d13988d8ecf8a3f97ecdd69d0390ce9
Status: Downloaded newer image for alpine:3.4
 ---> f64255f97787
...
Step 11/11 : CMD sh /usr/share/nginx/docker-run.sh
 ---> Running in a98dad172cbf
 ---> 4e2fec490452
Removing intermediate container a98dad172cbf
Successfully built 4e2fec490452
Successfully tagged swagger-editor:latest
```

At this point the Swagger Editor should be running on port 8080 of the localhost.

URL: [http://localhost:8000](http://localhost:8000)

### Removing the Editor

Attempts to stop and remove any swagger-editor related containers and images as well as remove the cloned Github repository.

From the `swagger-editor/` directory:

```
./remove-editor.sh
```

Example:

```
$ ./remove-editor.sh
swagger-editor
swagger-editor
Untagged: swagger-editor:latest
Deleted: sha256:4e2fec490452e2a5e7d8b5e7c60d00573871ae431a70e07956b11747a996218d
Deleted: sha256:30313f108daf89745df5cd9e9704df4ecd9bdec506c69d664f28e55f72b62a6e
Deleted: sha256:ef48c7b441e48f44a820a2e84545fb976a4e50aec65f3b664ba31a2a95e5af37
Deleted: sha256:23dc597c8c1ff1ded160f8958750832ba308f4e565df1ae813d27e32a183f3f4
Deleted: sha256:0689492762865185ad65ec4465087bdfc4bdf2728dab164083f67e1c3275a402
Deleted: sha256:c5aaa7b1bed1a3adf574d8b26f65479b647bcb537c827b37711a3f932a698481
Deleted: sha256:10965b12ad98641cd3b5c962fb949a406837577a187de6479738583f406ec041
Deleted: sha256:5d5d904e0494b11bdf8440e056171af9aefe8988512813f374bf670c0e49c447
Deleted: sha256:7415c08d7791b2897c5f99640d3fc07e2ffb3d76b6c0c0b7a9d3f59155fb36ba
Deleted: sha256:ae14e755b7e0acd0e794b8dddfa8b697923f1bd979ebde8e71a736cffac09822
Deleted: sha256:fa1c7282e45b132ab56317d92d613d5d81e88f5bfd43cf7ebca677977ee00a47
Deleted: sha256:4212dc426a078f63a9416ef7d4ee38f9cc441daf824fce01553f5c339c191f25
Deleted: sha256:96d031a270efc9bd51810328e4c5dab04e22ab161e1a2e4f79b6aaeb08385118
Deleted: sha256:08e43dd1b155e5106971f69ff5d06159dfaf8902477aed0f4508c10eab8fbc22
Deleted: sha256:40c150501113da37899b1296e343f96d579465d4972587ff7475fe77cc3368c4
Deleted: sha256:d3c965bf91afed6b1f3451b6c25679dc812a5ba137850bfd300154a78ceeb74b
Deleted: sha256:042e2065efd0486a9be8b56d0603a5d0d325fa4cd40f6630f233582bd0adb8e6
Untagged: alpine:3.4
Untagged: alpine@sha256:833ad81ace8277324f3ca8c91c02bdcf1d13988d8ecf8a3f97ecdd69d0390ce9
Deleted: sha256:f64255f977873799868dee1ea031058ec9bc3684351945a7d9980feffc80d996
Deleted: sha256:2b0fb280b60dad0c3e2f6b207ef0d8f6a04f09638d245d3a2fdf0d6933e734d6
```