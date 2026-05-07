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
                    $"Move disk 1 from {source} to {target}"
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
                $"Move disk {disks} from {source} to {target}"
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