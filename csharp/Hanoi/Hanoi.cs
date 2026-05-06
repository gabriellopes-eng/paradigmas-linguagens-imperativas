namespace HanoiNamespace
{
    public class Hanoi
    {
        public static void Solve(
            int disks,
            string source,
            string auxiliary,
            string target,
            List<string> moves
        )
        {
            if (disks == 1)
            {
                moves.Add(
                    $"Mover disco 1 de {source} para {target}"
                );

                return;
            }

            Solve(
                disks - 1,
                source,
                target,
                auxiliary,
                moves
            );

            moves.Add(
                $"Mover disco {disks} de {source} para {target}"
            );

            Solve(
                disks - 1,
                auxiliary,
                source,
                target,
                moves
            );
        }
    }
}