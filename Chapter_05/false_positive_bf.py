from base_bloomfilter import BloomFilter

bf = BloomFilter(10, 3)

bf.add("apple")
bf.add("banana")
bf.add("orange")

print(bf.contains("apple"))
print(bf.contains("banana"))
print(bf.contains("orange"))
print(bf.contains("grape"))
print(bf.contains("kiwi"))
