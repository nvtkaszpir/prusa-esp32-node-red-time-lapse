
variable "GIT_COMMIT" {
  default = "latest"
}
variable "GIT_SOURCE" {
  default = ""
}
group "default" {
  targets = [
    "node_red_amd64",
    "node_red_arm64",
    ]
}

target "node_red_amd64" {
  args = {
    GIT_COMMIT = "${GIT_COMMIT}"
    GIT_SOURCE = "${GIT_SOURCE}"
    ARCH = "amd64"
  }

  dockerfile = "Dockerfile"
  tags = ["nodered:${GIT_COMMIT}-amd64"]
  platforms = ["linux/amd64"]
}

target "node_red_arm64" {
  args = {
    GIT_COMMIT = "${GIT_COMMIT}"
    GIT_SOURCE = "${GIT_SOURCE}"
    ARCH = "arm64"
  }

  dockerfile = "Dockerfile"
  tags = ["nodered:${GIT_COMMIT}-arm64"]
  platforms = ["linux/arm64"]
}
