class Hanoi:

    @staticmethod
    def solve(disks, source, auxiliary, target):

        moves = []

        Hanoi.hanoi_recursive(
            disks,
            source,
            auxiliary,
            target,
            moves
        )

        return moves

    @staticmethod
    def hanoi_recursive(disks, source, auxiliary, target, moves):

        if disks == 1:

            moves.append(
                f"Mover disco 1 de {source} para {target}"
            )

            return

        Hanoi.hanoi_recursive(
            disks - 1,
            source,
            target,
            auxiliary,
            moves
        )

        moves.append(
            f"Mover disco {disks} de {source} para {target}"
        )

        Hanoi.hanoi_recursive(
            disks - 1,
            auxiliary,
            source,
            target,
            moves
        )