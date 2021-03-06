from Bio import SeqIO, Entrez, SeqRecord


def make_protein_record(nuc_record):
    """Returns a new SeqRecord with the translated sequence (default table)."""
    return SeqRecord(seq = nuc_record.seq.translate(), \
                     id = "trans_" + nuc_record.id, \
                     description = nuc_record.id)

hba1_protein = make_protein_record(SeqIO.read("./resc/HBA1.fasta","fasta"))
SeqIO.write(hba1_protein, "hba1protein.fasta", "fasta")

hba2_protein = make_protein_record(SeqIO.read("./resc/HBA2.fasta","fasta"))
SeqIO.write(hba2_protein, "hba2protein.fasta", "fasta")

ls_orchid_protein = (make_protein_record(nuc_rec) for nuc_rec in \
            SeqIO.parse("./resc/ls_orchid.fasta", "fasta"))
SeqIO.write(ls_orchid_protein, "ls_orchid_protein.fasta", "fasta")

fa_protein = (make_protein_record(nuc_rec) for nuc_rec in \
            SeqIO.parse("./resc/fa.fasta", "fasta"))
SeqIO.write(fa_protein, "fa_protein.fasta", "fasta")