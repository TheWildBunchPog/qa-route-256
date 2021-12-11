package database

import (
	"context"
	"time"

	"gitlab.ozon.dev/qa/teachers/qa-route-256/item-api/internal/models"
)

func (db *DB) InsertItem(ctx context.Context, item *models.Item) (int64, error) {
	query := `INSERT INTO items (title, description)
	VALUES ($1, $2)
	RETURNING id;
`
	ctx, cancel := context.WithTimeout(ctx, 10*time.Second)
	defer cancel()
	var id int64
	err := db.QueryRowContext(
		ctx,
		query,
		item.Title,
		item.Description,
	).Scan(
		&id,
	)
	if err != nil {
		return 0, err
	}
	return id, nil
}
