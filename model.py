import torch
import torch.nn as nn


class PhysicalModel(torch.nn.Module):
    def __init__(self, latitude):
        super(PhysicalModel, self).__init__()
        self.pi = 3.1416
        self.capacity = torch.nn.Parameter(torch.tensor(1.0), requires_grad=True)
        self.alpha = torch.nn.Parameter(torch.tensor(1.0), requires_grad=True)
        self.beta = torch.nn.Parameter(
            torch.tensor(latitude * self.pi / 180), requires_grad=True
        )
        self.gamma = torch.nn.Parameter(torch.tensor(self.pi), requires_grad=True)
        self.gamma_bt = torch.nn.Parameter(torch.tensor(0.74), requires_grad=False)
        self.rho = torch.nn.Parameter(torch.tensor(0.20), requires_grad=False)
        self.tem = torch.nn.Parameter(torch.tensor(0.005), requires_grad=False)
        self.noct = torch.nn.Parameter(torch.tensor(48), requires_grad=False)

    def forward(self, x):
        I_bt = x[:, 9] * self.gamma_bt * torch.sin(x[:, 13])
        I_pv = (
            x[:, 9]
            * self.gamma_bt
            * (
                torch.sin(x[:, 13]) * torch.cos(self.beta)
                + torch.cos(x[:, 13])
                * torch.sin(self.beta)
                * torch.cos(self.gamma - x[:, 14])
            )
            + x[:, 8] * ((1 + torch.cos(self.beta)) / 2)
            + (I_bt + x[:, 8]) * self.rho * (1 - torch.cos(self.beta)) / 2
        )
        T_pv = x[:, 6] + I_pv / 800 * (self.noct - 20)
        out = self.capacity * I_pv / 1000 * (1 - self.tem * (T_pv - 25))
        return out
