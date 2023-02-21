from conformer_handler import *
import os
import sys
sys.path.append(r'C:\Users\edens\Documents\GitHub\Conformers_code-main\utils')
import tab_data
import help_functions

if __name__ == '__main__':
    os.chdir(r'C:\Users\edens\Documents\GitHub\Conformers_code-main\xyz_files')
    analyze_conformers(r'C:\Users\edens\Documents\GitHub\Conformers_code-main\xyz_files\danilo', 'crest_conformers.xyz',
                       'xyz')

    # os.chdir(r'C:\Users\edens\Documents\GitHub\Conformers_code-main\xyz_files\danilo\PB_R_C_2_472_ox')
    # crest_conformers = Conformers('crest_conformers.xyz', 'xyz')
    # data = tab_data.TabDataAnalyzer(parser=tab_data.set_tab_parser(), origin_df=crest_conformers.coordinates_df_list[1],
    #                                 xyz_filename='conformer', get_plot=True)
    # overlay_analyzer = tab_data.OverlayAnalyzer(parser=tab_data.set_overlay_parser(), xyz_filenames=['0', '1'],
    #                                             xyz_dfs=[crest_conformers.coordinates_df_list[0],
    #                                                      crest_conformers.coordinates_df_list[1]], fit_mode='all', )
#                                         atoms=['30', '20', '16', '0', '24', '8', '5', '33'],

