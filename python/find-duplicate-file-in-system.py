class Solution:
    def split_filename_content(file_name_content: str) -> (str, str):
        separate_index = file_name_content.find("(")
        file_name = file_name_content[:separate_index]
        content = file_name_content[separate_index + 1:]
        return file_name, content

    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_to_files = defaultdict(list)
        for path in paths:
            path_split = path.split(" ")
            directory = path_split[0]
            for i in range(1, len(path_split)):
                file_name, content = Solution.split_filename_content(path_split[i])
                content_to_files[content].append(f"{directory}/{file_name}")
        return [content_to_files[content] for content in content_to_files if 1 < len(content_to_files[content])]
