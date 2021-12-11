package unit

import (
	"github.com/stretchr/testify/assert"
	"reflect"
	"testing"
)

func BenchmarkUnique(b *testing.B) {
	slice := []int{2, 2, 2, 7, 1, 2, 4, 4, 4, 22, 22, 5, 8, 0, 11, 113}

	b.Run("1", func(b *testing.B) {
		for i := 0; i < b.N; i++ {
			unique1(slice)
		}
	})
	b.Run("2", func(b *testing.B) {
		for i := 0; i < b.N; i++ {
			unique2(slice)
		}
	})
	b.Run("3", func(b *testing.B) {
		for i := 0; i < b.N; i++ {
			unique3(slice)
		}
	})
}

func TestUnique(t *testing.T) {
	t.Run("all values are unique\n", func(t *testing.T) {
		t.Parallel()

		want := []int{1, 2, 3}

		got := unique2([]int{1, 2, 3})

		t.Logf("got = %d", got)
		assert.True(t, reflect.DeepEqual(want, got))
	})

	t.Run("one value not unique", func(t *testing.T) {
		t.Parallel()

		want := []int{8, 2, 1}

		got := unique2([]int{8, 8, 2, 1})

		t.Logf("got = %d", got)
		assert.True(t, reflect.DeepEqual(want, got))
	})

	t.Run("many values not unique", func(t *testing.T) {
		t.Parallel()

		want := []int{2, 7, 1, 4, 22, 5, 8, 0, 11, 113}

		got := unique2([]int{2, 2, 2, 7, 1, 2, 4, 4, 4, 22, 22, 5, 8, 0, 11, 113})

		t.Logf("got = %d", got)
		assert.True(t, reflect.DeepEqual(want, got))
	})
}

