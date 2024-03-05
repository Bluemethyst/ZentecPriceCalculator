package main

import (
	"embed"
	"fmt"
	"os"
	"strconv"
	"strings"

	"github.com/fatih/color"
)

//go:embed art.txt
var bannerContent embed.FS

func banner() {
	b, err := bannerContent.ReadFile("art.txt")
	if err != nil {
		panic(err)
	}
	fmt.Println(string(b))
}

func main() {
	// Decoration, ignore this
	banner()

	color.HiBlue("Created by Caleb")

	color.Red("Press 'q' or 'Ctrl + C' anytime to exit.")

	// Loop the program until q or Ctrl + C is pressed
	for {
		color.New(color.FgCyan).Print("Input Value... ")
		var inputStr string
		fmt.Scanln(&inputStr)
		inputStr = strings.ToLower(inputStr)

		// Check to see if the input is a Q for exiting
		if inputStr == "q" {
			os.Exit(0)
		}
		if inputStr == "hello" {
			color.Yellow("Hey adrian :D")
			continue
		}
		// Check to see if the input is a number
		inputFloat, err := strconv.ParseFloat(inputStr, 64)
		if err != nil {
			color.Red("Error: Please enter a valid number.")
			continue
		}

		// Check to see what multiple the input needs to be multiplied by
		// This part is simplified for brevity. You can add more conditions as needed.
		if inputFloat < 10 {
			fmt.Printf("%.2f\n", inputFloat*2)
		} else if inputFloat < 15 {
			fmt.Printf("%.2f\n", inputFloat*1.9)
		} else if inputFloat < 20 {
			fmt.Printf("%.2f\n", inputFloat*1.8)
		} else if inputFloat < 25 {
			fmt.Printf("%.2f\n", inputFloat*1.75)
		} else if inputFloat < 30 {
			fmt.Printf("%.2f\n", inputFloat*1.7)
		} else if inputFloat < 35 {
			fmt.Printf("%.2f\n", inputFloat*1.65)
		} else if inputFloat < 40 {
			fmt.Printf("%.2f\n", inputFloat*1.6)
		} else if inputFloat < 45 {
			fmt.Printf("%.2f\n", inputFloat*1.55)
		} else if inputFloat < 60 {
			fmt.Printf("%.2f\n", inputFloat*1.5)
		} else if inputFloat < 70 {
			fmt.Printf("%.2f\n", inputFloat*1.48)
		} else if inputFloat < 80 {
			fmt.Printf("%.2f\n", inputFloat*1.47)
		} else if inputFloat < 90 {
			fmt.Printf("%.2f\n", inputFloat*1.46)
		} else if inputFloat < 100 {
			fmt.Printf("%.2f\n", inputFloat*1.45)
		} else if inputFloat < 110 {
			fmt.Printf("%.2f\n", inputFloat*1.44)
		} else if inputFloat < 120 {
			fmt.Printf("%.2f\n", inputFloat*1.43)
		} else if inputFloat < 130 {
			fmt.Printf("%.2f\n", inputFloat*1.42)
		} else if inputFloat < 140 {
			fmt.Printf("%.2f\n", inputFloat*1.41)
		} else if inputFloat < 150 {
			fmt.Printf("%.2f\n", inputFloat*1.4)
		} else if inputFloat < 160 {
			fmt.Printf("%.2f\n", inputFloat*1.39)
		} else if inputFloat < 170 {
			fmt.Printf("%.2f\n", inputFloat*1.38)
		} else if inputFloat < 180 {
			fmt.Printf("%.2f\n", inputFloat*1.37)
		} else if inputFloat < 190 {
			fmt.Printf("%.2f\n", inputFloat*1.36)
		} else if inputFloat < 200 {
			fmt.Printf("%.2f\n", inputFloat*1.35)
		} else if inputFloat < 225 {
			fmt.Printf("%.2f\n", inputFloat*1.345)
		} else if inputFloat < 250 {
			fmt.Printf("%.2f\n", inputFloat*1.34)
		} else if inputFloat < 300 {
			fmt.Printf("%.2f\n", inputFloat*1.335)
		} else if inputFloat < 375 {
			fmt.Printf("%.2f\n", inputFloat*1.33)
		} else if inputFloat < 475 {
			fmt.Printf("%.2f\n", inputFloat*1.325)
		} else if inputFloat < 550 {
			fmt.Printf("%.2f\n", inputFloat*1.32)
		} else if inputFloat < 650 {
			fmt.Printf("%.2f\n", inputFloat*1.315)
		} else if inputFloat < 750 {
			fmt.Printf("%.2f\n", inputFloat*1.31)
		} else if inputFloat < 850 {
			fmt.Printf("%.2f\n", inputFloat*1.305)
		} else if inputFloat < 1000 {
			fmt.Printf("%.2f\n", inputFloat*1.3)
		} else if inputFloat < 1100 {
			fmt.Printf("%.2f\n", inputFloat*1.295)
		} else if inputFloat < 1200 {
			fmt.Printf("%.2f\n", inputFloat*1.29)
		} else if inputFloat < 1300 {
			fmt.Printf("%.2f\n", inputFloat*1.285)
		} else if inputFloat < 1400 {
			fmt.Printf("%.2f\n", inputFloat*1.28)
		} else if inputFloat < 1500 {
			fmt.Printf("%.2f\n", inputFloat*1.275)
		} else if inputFloat < 1600 {
			fmt.Printf("%.2f\n", inputFloat*1.27)
		} else if inputFloat < 1700 {
			fmt.Printf("%.2f\n", inputFloat*1.265)
		} else if inputFloat < 1800 {
			fmt.Printf("%.2f\n", inputFloat*1.26)
		} else if inputFloat < 1900 {
			fmt.Printf("%.2f\n", inputFloat*1.225)
		} else if inputFloat < 2000 {
			fmt.Printf("%.2f\n", inputFloat*1.25)
		} else if inputFloat > 1999.99 {
			fmt.Printf("%.2f\n", inputFloat*1.2)
		} else if inputFloat == 0 {
			fmt.Println("An expected error occured, stop trying to multiply by zero man you already know the answer")
		}
	}
}
