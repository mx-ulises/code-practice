class Solution:
    def get_tile_arrangements(tile_count, preffix: str, available_tiles) -> int:
        if available_tiles == 0:
            return 0
        tile_arrangements = 0
        for tile in tile_count:
            if tile_count[tile] == 0:
                continue
            tile_count[tile] -= 1
            tile_arrangements += 1 + Solution.get_tile_arrangements(tile_count, preffix + tile, available_tiles - 1)
            tile_count[tile] += 1
        return tile_arrangements

    def numTilePossibilities(self, tiles: str) -> int:
        tile_count = defaultdict(lambda: 0)
        for tile in tiles:
            tile_count[tile] += 1
        return Solution.get_tile_arrangements(tile_count, "", len(tiles))
