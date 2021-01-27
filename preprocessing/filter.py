import json
import gzip
import io

paper_ids_to_keep = set()
with gzip.open('20200705v1/full/metadata/metadata_0.jsonl.gz', 'rb') as gz, open('20200705v1/full/metadata/metadata_0_filtered.jsonl', 'wb') as f_out:
    f = io.BufferedReader(gz)
    for line in f.readlines():
        metadata_dict = json.loads(line)
        paper_id = metadata_dict['paper_id']
        mag_field_of_study = metadata_dict['mag_field_of_study']
        if mag_field_of_study and 'Computer Science' in mag_field_of_study:
            paper_ids_to_keep.add(paper_id)
            f_out.write(line)


# now, we get those papers' full text
with gzip.open(batch['input_pdf_parses_path'], 'rb') as gz, open(batch['output_pdf_parses_path'], 'wb') as f_out:
    f = io.BufferedReader(gz)
    for line in f.readlines():
        metadata_dict = json.loads(line)
        paper_id = metadata_dict['paper_id']
        if paper_id in paper_ids_to_keep:
            f_out.write(line)

