package main

import (
	"fmt"
	"observer/youtube"
)

func main()	{
	fmt.Println("Running pubsub test")
	LarryWheels := youtube.Creator{Name: "Larry Wheels",}

	Josh := youtube.Viewer{Name: "Josh Mogil from New Jersey"}
	Richard := youtube.Viewer{Name: "Richard I from PA"}

	Josh.Subscribe(&LarryWheels)
	Richard.Subscribe(&LarryWheels)

	LarryWheels.Publish()
}