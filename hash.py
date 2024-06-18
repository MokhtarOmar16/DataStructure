class Hash:

  def Hash32(self, strInput):
    OffsetBasis = 2166136261
    FNVPrime = 16777619

    data = strInput.encode('ascii')

    hash = OffsetBasis

    for i in range(len(data)):
      hash = hash ^ data[i]
      hash = hash * FNVPrime

    print(strInput + ", " + str(hash) + ", " + hex(hash))

    return hash

  def Hash64(self, strInput):
    OffsetBasis = 14695981039346656037
    FNVPrime = 1099511628211

    data = strInput.encode('ascii')

    hash = OffsetBasis

    for i in range(len(data)):
      hash = hash ^ data[i]
      hash = hash * FNVPrime

    print(strInput + ", " + str(hash) + ", " + hex(hash))

    return hash
