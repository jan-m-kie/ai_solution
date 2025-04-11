terraform {
  backend "gcs" {
    bucket = "terraform-ai-solution-state"
    prefix = "terraform/state"
  }

  required_providers {
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "~> 2.0"
    }
  }
}

provider "kubernetes" {
  config_path = var.kubeconfig_path
}

variable "kubeconfig_path" {
  type        = string
  description = "Path to the kubeconfig file"
}

resource "kubernetes_namespace" "ai_solution" {
  metadata {
    name = "ai-solution"
    labels = {
      environment = "dev"
      team        = "ai"
    }
  }

  lifecycle {
    ignore_changes = all
  }
}
