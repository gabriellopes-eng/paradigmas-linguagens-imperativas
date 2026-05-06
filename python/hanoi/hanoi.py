class Hanoi:

    @staticmethod
    def solve(disks, source, auxiliary, target):

        moves = []

        Hanoi._hanoi_recursive(
            disks,
            source,
            auxiliary,
            target,
            moves
        )

        return moves

    @staticmethod
    def _hanoi_recursive(disks, source, auxiliary, target, moves):

        if disks == 1:

            moves.append(
                f"Mover disco 1 de {source} para {target}"
            )

            return

        Hanoi._hanoi_recursive(
            disks - 1,
            source,
            target,
            auxiliary,
            moves
        )

        moves.append(
            f"Mover disco {disks} de {source} para {target}"
        )

        Hanoi._hanoi_recursive(
            disks - 1,
            auxiliary,
            source,
            target,
            moves
        )