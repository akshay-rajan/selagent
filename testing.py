import sys
import helpers

if __name__ == "__main__":
    ans = helpers.get_elements_by_id(sys.argv[1], sys.argv[2])
    # ans = helpers.get_text_content(sys.argv[1])
    print(ans)
