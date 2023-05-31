# Generated by Django 4.1.7 on 2023-04-06 15:09

from django.db import migrations, models

import api_app.fields


class Migration(migrations.Migration):

    dependencies = [
        ('analyzers_manager', '0015_alter_analyzerconfig_disabled_in_organizations_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analyzerconfig',
            name='not_supported_filetypes',
            field=api_app.fields.ChoiceArrayField(base_field=models.CharField(choices=[('application/w-script-file', 'Wscript'), ('application/javascript', 'Javascript1'), ('application/x-javascript', 'Javascript2'), ('text/javascript', 'Javascript3'), ('application/x-vbscript', 'Vb Script'), ('text/x-ms-iqy', 'Iqy'), ('application/vnd.android.package-archive', 'Apk'), ('application/x-dex', 'Dex'), ('application/onenote', 'One Note'), ('android', 'Android'), ('application/zip', 'Zip1'), ('multipart/x-zip', 'Zip2'), ('application/java-archive', 'Java'), ('text/rtf', 'Rtf1'), ('application/rtf', 'Rtf2'), ('application/x-dosexec', 'Dos'), ('application/x-sharedlib', 'Shared Lib'), ('application/x-executable', 'Exe'), ('application/x-elf', 'Elf'), ('application/octet-stream', 'Octet'), ('application/vnd.tcpdump.pcap', 'Pcap'), ('application/pdf', 'Pdf'), ('text/html', 'Html'), ('application/x-mspublisher', 'Pub'), ('application/vnd.ms-excel.addin.macroEnabled', 'Excel Macro1'), ('application/vnd.ms-excel.sheet.macroEnabled.12', 'Excel Macro2'), ('application/vnd.ms-excel', 'Excel1'), ('application/excel', 'Excel2'), ('application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', 'Doc'), ('application/xml', 'Xml1'), ('text/xml', 'Xml2'), ('application/encrypted', 'Encrypted'), ('text/plain', 'Plain'), ('text/csv', 'Csv'), ('application/vnd.openxmlformats-officedocument.presentationml.presentation', 'Pptx'), ('application/msword', 'Word1'), ('application/vnd.openxmlformats-officedocument.wordprocessingml.document', 'Word2'), ('application/vnd.ms-powerpoint', 'Powerpoint'), ('application/vnd.ms-office', 'Office'), ('application/x-binary', 'Binary'), ('application/x-macbinary', 'Mac1'), ('application/mac-binary', 'Mac2'), ('application/x-mach-binary', 'Mac3'), ('application/x-zip-compressed', 'Compress1'), ('application/x-compressed', 'Compress2')], max_length=90), blank=True, default=list, size=None),
        ),
        migrations.AlterField(
            model_name='analyzerconfig',
            name='supported_filetypes',
            field=api_app.fields.ChoiceArrayField(base_field=models.CharField(choices=[('application/w-script-file', 'Wscript'), ('application/javascript', 'Javascript1'), ('application/x-javascript', 'Javascript2'), ('text/javascript', 'Javascript3'), ('application/x-vbscript', 'Vb Script'), ('text/x-ms-iqy', 'Iqy'), ('application/vnd.android.package-archive', 'Apk'), ('application/x-dex', 'Dex'), ('application/onenote', 'One Note'), ('android', 'Android'), ('application/zip', 'Zip1'), ('multipart/x-zip', 'Zip2'), ('application/java-archive', 'Java'), ('text/rtf', 'Rtf1'), ('application/rtf', 'Rtf2'), ('application/x-dosexec', 'Dos'), ('application/x-sharedlib', 'Shared Lib'), ('application/x-executable', 'Exe'), ('application/x-elf', 'Elf'), ('application/octet-stream', 'Octet'), ('application/vnd.tcpdump.pcap', 'Pcap'), ('application/pdf', 'Pdf'), ('text/html', 'Html'), ('application/x-mspublisher', 'Pub'), ('application/vnd.ms-excel.addin.macroEnabled', 'Excel Macro1'), ('application/vnd.ms-excel.sheet.macroEnabled.12', 'Excel Macro2'), ('application/vnd.ms-excel', 'Excel1'), ('application/excel', 'Excel2'), ('application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', 'Doc'), ('application/xml', 'Xml1'), ('text/xml', 'Xml2'), ('application/encrypted', 'Encrypted'), ('text/plain', 'Plain'), ('text/csv', 'Csv'), ('application/vnd.openxmlformats-officedocument.presentationml.presentation', 'Pptx'), ('application/msword', 'Word1'), ('application/vnd.openxmlformats-officedocument.wordprocessingml.document', 'Word2'), ('application/vnd.ms-powerpoint', 'Powerpoint'), ('application/vnd.ms-office', 'Office'), ('application/x-binary', 'Binary'), ('application/x-macbinary', 'Mac1'), ('application/mac-binary', 'Mac2'), ('application/x-mach-binary', 'Mac3'), ('application/x-zip-compressed', 'Compress1'), ('application/x-compressed', 'Compress2')], max_length=90), blank=True, default=list, size=None),
        ),
    ]
