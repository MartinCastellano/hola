package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {

	scanner := bufio.NewScanner(os.Stdin)
	fmt.Printf("ano de nacimiento ")
	scanner.Scan()
	input, _ := strconv.ParseInt(scanner.Text(), 10, 64)

	fmt.Printf("tendras  %d al final del 2020 ", 2020-input)

}

// go build hello.go / go run hello.go
// --> /.hello
