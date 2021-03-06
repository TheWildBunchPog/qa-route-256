//go:build integration
// +build integration

package tests

import (
	"context"
	"fmt"
	"testing"

	item "gitlab.ozon.dev/qa/teachers/qa-route-256/item-api/pkg/api"
	"gitlab.ozon.dev/qa/teachers/qa-route-256/item-api/test/internal/config"
	"google.golang.org/grpc"
)

var (
	ctx        context.Context
	itemClient item.ItemClient
)

func TestMain(m *testing.M) {
	cfg := config.ProcessConfig()
	ctx = context.Background()

	conn, err := grpc.Dial(
		cfg.Host,
		grpc.WithInsecure(),
	)
	if err != nil {
		panic(fmt.Errorf("grpc.Dial() err: %v", err))
	}
	defer conn.Close()

	itemClient = item.NewItemClient(conn)

	m.Run()
}
