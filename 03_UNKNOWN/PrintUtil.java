	PrintUtil {

		private void print(Object x) {
			System.out.println(x.toString());
		}

		private void print(Object[] array) {
			System.out.println(Arrays.toString(array));
		}

		private void print(Object[][] array2d) {

			if (array2d == null) {
				return;
			}

			for (int i = 0 ; i < array2d.length; i++) {

				if (array2d[i] == null) {
					continue;
				}

				print(array2d[i]);
			}
			System.out.println();
		}

		private void print(Map map) {

			for (Object key: map.keySet()) {
				Object val = map.get(key);
				if (val instanceof int[]) {
					int[] array = (int[]) val;
					print("Key: " + key + " Value: " + Arrays.toString(array));
				} else {
					print("Key: " + key + " Value: " + val);
				}
			}
		}
	}


