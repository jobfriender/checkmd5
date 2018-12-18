package main

import (
	"crypto/md5"
	"fmt"
	"io"
	"io/ioutil"
	"log"
	"os"
)

func main() {

	data, err := ioutil.ReadFile(os.Args[1])
	
	if err != nil {
		log.Fatal(err)
	}
	
	h := md5.New()
	io.WriteString(h, string(data))

	fmt.Printf("%x", h.Sum(nil))
	fmt.Printf("\n\r")

}
