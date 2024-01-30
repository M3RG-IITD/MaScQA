from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
from bs4 import BeautifulSoup

def blast(seq):
    '''
    Returns MSA with a BLAST search. Uses beautiful soup
    to parse result.

    1. import packages
    2. Submit BLAST search with sequences
    3. Get result
    4. Parse MSA
    5. Return a tuple of e score, id of top match
    '''
    # Submit BLAST search with sequences
    result_handle = NCBIWWW.qblast("blastp", "nr", seq)

    # Get result
    blast_record = NCBIXML.read(result_handle)

    # Parse MSA
    soup = BeautifulSoup(blast_record, 'html.parser')
    top_match = soup.find('hit')
    e = top_match.find('hsp_evalue').text
    id = top_match.find('hit_id').text

    return e, id