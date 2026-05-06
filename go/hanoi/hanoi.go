package hanoi

import "fmt"

func Solve(
	disks int,
	source string,
	auxiliary string,
	target string,
	moves *[]string,
) {

	if disks == 1 {

		*moves = append(
			*moves,
			fmt.Sprintf(
				"Mover disco 1 de %s para %s",
				source,
				target,
			),
		)

		return
	}

	Solve(
		disks-1,
		source,
		target,
		auxiliary,
		moves,
	)

	*moves = append(
		*moves,
		fmt.Sprintf(
			"Mover disco %d de %s para %s",
			disks,
			source,
			target,
		),
	)

	Solve(
		disks-1,
		auxiliary,
		source,
		target,
		moves,
	)
}
