//go:build integration
// +build integration

package tests

import (
	"reflect"
	"testing"

	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"
	item "gitlab.ozon.dev/qa/teachers/qa-route-256/item-api/pkg/api"
	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/status"
)

func TestGetItem(t *testing.T) {
	testCases := []struct {
		name        string
		title       string
		description string
	}{
		{
			"get default request should pass",
			"test title",
			"test description",
		},
		{
			"get long title should pass",
			"This is most longest title in the world!",
			"test description",
		},
		{
			"get multiline description should pass",
			"test title",
			`This is most longest description in the world! OMG!!!
This is most longest description in the world! OMG!!! 
This is most longest description in the world! OMG!!! 
This is most longest description in the world! OMG!!! 
This is most longest description in the world! OMG!!! 
This is most longest description in the world! OMG!!! 
`,
		},
	}
	for _, tc := range testCases {
		tc := tc
		t.Run(tc.name, func(t *testing.T) {
			t.Parallel()

			create_item := item.CreateItemRequest{
				Title:       tc.title,
				Description: tc.description,
			}

			item_response, err := itemClient.CreateItem(ctx, &create_item)
			require.NoError(t, err)

			get_item := item.GetItemRequest{
				Id:       item_response.Id,
			}

			get_item_response, err := itemClient.GetItem(ctx, &get_item)
			require.NoError(t, err)

			assert.True(t, reflect.DeepEqual(tc.title, get_item_response.Title))
			assert.True(t, reflect.DeepEqual(tc.description, get_item_response.Description))
		})
	}

	t.Run("failed to get item\n", func(t *testing.T) {

		get_item := item.GetItemRequest{
			Id:       60,
		}

		_, err := itemClient.GetItem(ctx, &get_item)

		require.Error(t, err)
		assert.Equal(t, codes.Unknown.String(), status.Code(err).String())
	})
}
