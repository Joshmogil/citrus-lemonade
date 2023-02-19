package main

import (
	"log"
	"net"
	"fmt"

	"google.golang.org/grpc"
)

func main() {
	fmt.Printf("Starting server!")
	lis, err := net.Listen("tcp", ":9000")
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}

	grpcServer := grpc.NewServer()

	if err := grpcServer.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %s", err)
	}
}