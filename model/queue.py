class Queue:
    unlimited = False
    limit = 0
    λ = 0
    µ = 0
    ρ = 0

    def __init__(self, unlimited, λ, µ, limit = 0):
        self.unlimited = unlimited
        self.λ = λ
        self.µ = µ
        self.limit = limit
        self.ρ = self.get_ro()

    def get_ro(self):
        ρ = self.λ / self.µ
        return ρ
