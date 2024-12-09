from huffman import build_huffman_tree, generate_codes


def compress(text, codes):
    compressed = []
    for char in text:
        compressed.extend(codes[char])

    compressed_bits = "".join(compressed)
    extra_padding = 8 - len(compressed_bits) % 8
    compressed_bits += "0" * extra_padding

    compressed_bytearray = bytearray()
    for i in range(0, len(compressed_bits), 8):
        byte = compressed_bits[i : i + 8]
        compressed_bytearray.append(int(byte, 2))

    return compressed_bytearray, extra_padding


def decompress(compressed, codes, extra_padding):
    compressed_bits = "".join(f"{byte:08b}" for byte in compressed)
    compressed_bits = compressed_bits[:-extra_padding]

    reversed_codes = {code: char for char, code in codes.items()}
    result = []
    current_code = ""
    for bit in compressed_bits:
        current_code += bit
        if current_code in reversed_codes:
            result.append(reversed_codes[current_code])
            current_code = ""
    return "".join(result)


if __name__ == "__main__":
    text = "abracadabra simsalabim"
    root = build_huffman_tree(text)
    codes = generate_codes(root)
    print(f"Коди Гаффмана: {codes}")

    compressed, extra_padding = compress(text, codes)
    print(f"Стиснутий текст (у байтах): {list(compressed)}, {extra_padding}")

    decompressed = decompress(compressed, codes, extra_padding)
    print(f"Розпакований текст: {decompressed}")

    original_size = len(text) * 8
    compressed_size = len(compressed) * 8 - extra_padding
    print(f"Оригінальний розмір: {original_size} біт")
    print(f"Розмір після стиснення: {compressed_size} біт")
    print(f"Коефіцієнт стиснення: {original_size / compressed_size:.2f}")
