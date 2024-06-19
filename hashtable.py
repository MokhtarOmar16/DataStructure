

class KeyValuePair:

    def __init__(self, Key, value):
      self.Key = Key
      self.Value = value


class HashTable:

  def __init__(self):
    self.initial_size = 3
    self.entries_count = 0
    self.entries = [None] * self.initial_size

  def get_hash(self, Key):
    # using FNV-1a hash function to generate a hash value
    fnv_offset_basis = 2166136261
    fnv_prime = 16777619

    # convert Key to bytes and hash it
    data = str(Key).encode('ascii')
    hash_value = fnv_offset_basis

    for byte in data:
      hash_value ^= byte
      hash_value *= fnv_prime

    # return the hash value modulo the length of the entries array
    return hash_value % len(self.entries)

  def collision_handling(self, Key, hash_value, set):
    # handling collisions using linear probing
    for i in range(1, len(self.entries)):
      new_hash = (hash_value + i) % len(self.entries)

      print("[coll] " + str(Key) + " " + str(hash_value) + ", new hash: " +
            str(new_hash))
      if set and (self.entries[new_hash] is None
                  or self.entries[new_hash].Key == Key):
        return new_hash
      elif not set and self.entries[new_hash] and self.entries[
          new_hash].Key == Key:
        return new_hash

    return -1

  def add_to_entries(self, Key, value):
    # add Key-value pair to the entries array
    hash_value = self.get_hash(Key)

    if self.entries[
        hash_value] is not None and self.entries[hash_value].Key != Key:
      # collision occurred, resolve it using collision handling function
      hash_value = self.collision_handling(Key, hash_value, set=True)

    if hash_value == -1:
      raise Exception("Invalid Hashtable!!!!")

    if self.entries[hash_value] is None:
      # add new Key-value pair
      new_pair = KeyValuePair(Key, value)
      self.entries[hash_value] = new_pair
      self.entries_count += 1
    elif self.entries[hash_value].Key == Key:
      # update existing value for the given Key
      self.entries[hash_value].value = value
    else:
      raise Exception("Invalid Hashtable!!!!")

  def resize_or_not(self):
    # check if the entries array needs to be resized
    if self.entries_count < len(self.entries):
      return

    # double the size of the entries array and rehash all Key-value pairs
    new_size = len(self.entries) * 2
    entries_copy = self.entries.copy()
    self.entries = [None] * new_size
    self.entries_count = 0

    for i in range(len(entries_copy)):
      if entries_copy[i] is None:
        continue

      self.add_to_entries(entries_copy[i].Key, entries_copy[i].Value)

  def get(self, Key):
    # get value for the given Key
    hash_value = self.get_hash(Key)

    if self.entries[
        hash_value] is not None and self.entries[hash_value].Key != Key:
      # collision occurred, resolve it using collision handling function
      hash_value = self.collision_handling(Key, hash_value, set=False)

    if hash_value == -1 or self.entries[hash_value] is None:
      return None

    if self.entries[hash_value].Key == Key:
      return self.entries[hash_value].Value
    else:
      raise Exception("Invalid Hashtable!!!!")

  def set(self, key, value):
    self.resize_or_not()
    self.add_to_entries(key, value)

  def size(self):
    # return the number of Key-value pairs in the hash table
    return self.entries_count

  def print(self):
    # Print separator and table size
    print("-----------")
    print("[Size] " + str(self.size()))

    # Loop through all the entries in the hash table
    for i in range(len(self.entries)):
      if self.entries[i] is None:
        # If the entry is empty, print its index and 'null'
        print("[" + str(i) + "] null")
      else:
        # If the entry is not empty, print its index, Key, and value
        print("[" + str(i) + "] " + self.entries[i].Key + ":" +
              self.entries[i].Value)

    # Print separator
    print("============")

  # Define a nested KeyValuePair class to store Key-value pairs

