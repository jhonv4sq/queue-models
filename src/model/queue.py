class Queue:
    unlimited = False
    limit = 0
    server = 0
    λ = 0
    µ = 0
    ρ = 0

    def __init__(self, unlimited, λ, µ, server=1, limit=0):
        self.unlimited = unlimited
        self.server = server
        self.λ = λ
        self.µ = µ
        self.limit = limit
        self.ρ = self.get_rho()

    def get_rho(self):
        ρ = self.λ / self.µ
        return ρ
