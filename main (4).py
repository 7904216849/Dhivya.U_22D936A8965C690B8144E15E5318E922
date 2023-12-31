def linear_search_product(product_list, target_product):
  indices = []
  for index, product in enumerate(product_list):
    if product == target_product:
      indices.append(index)
  return indices


# Test the function with a list of products
if __name__ == "__main__":
  products = ["Apple", "Banana", "Orange", "Apple", "Grapes", "Apple"]
  target = "Apple"

  result = linear_search_product(products, target)

  if result:
    print(f"The target product '{target}' was found at indices: {result}")
  else:
    print(f"The target product '{target}' was not found in the list.")
