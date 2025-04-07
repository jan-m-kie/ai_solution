terraform {
  required_providers {
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "~> 2.0"
    }
  }
}

provider "kubernetes" {
  config_path = "~/.kube/config"
}

resource "kubernetes_namespace" "ai_solution" {
  metadata {
    name = "ai-solution"
    labels = {
      environment = "dev"
      team        = "ai"
    }
  }
}
