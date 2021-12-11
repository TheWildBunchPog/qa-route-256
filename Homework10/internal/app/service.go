package app

import (
	"gitlab.ozon.dev/qa/teachers/qa-route-256/item-api/internal/database"
	pb "gitlab.ozon.dev/qa/teachers/qa-route-256/item-api/pkg/api"
	"google.golang.org/grpc"
)

// ItemService ...
type ItemService struct {
	pb.ItemServer
	DB database.Database
}

// NewItemService ...
func NewItemService(db database.Database) *ItemService {
	return &ItemService{DB: db}
}

// RegisterNewItemService ...
func RegisterNewItemService(s *grpc.Server, db database.Database) {
	pb.RegisterItemServer(s, NewItemService(db))
}
