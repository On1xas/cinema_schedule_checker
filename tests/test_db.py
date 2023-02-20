import datetime
import sqlite3
from data.database_commands import clear_parsing_all_table

# show=('mooon в ТРЦ Palazzo', 'Зал 7 Visa Premiere', '2023-2-14T11:10:00', ' Мой домашний крокодил ', '2D')
# show_set={' Одиноки вместе ', ' Амстердам ', ' Операция «Фортуна»: Искусство побеждать ', ' mooon LOVE PARTY ', ' Форма голоса (RU SUB) ', ' Заклятие Абизу ', ' Мой домашний крокодил ', ' Свободные отношения ', ' Кот в сапогах 2: Последнее желание ', ' Непослушная ', ' М3ГАН ', ' Аватар: Путь воды ', ' Изумительный Морис ', ' Форма голоса ', ' Чебурашка ', ' Знакомство родителей '}
# show_set_api = {' Непослушная ', ' Форма голоса ', ' Аватар: Путь воды ', ' Одиноки вместе ', ' Мой домашний крокодил ',
#                 ' Изумительный Морис ', ' Операция «Фортуна»: Искусство побеждать ', ' М3ГАН ',
#                 ' Кот в сапогах 2: Последнее желание ', ' mooon LOVE PARTY ', ' Заклятие Абизу ',
#                 ' Знакомство родителей ', ' Амстердам ', ' Свободные отношения ', ' Форма голоса (RU SUB) ',
#                 ' Чебурашка '}
# show_set_db = {' Непослушная ', ' Форма голоса ', ' Одиноки вместе ', ' Аватар: Путь воды ', ' Мой домашний крокодил ',
#                ' Операция «Фортуна»: Искусство побеждать ', ' Изумительный Морис ', ' М3ГАН ',
#                ' Кот в сапогах 2: Последнее желание ', ' mooon LOVE PARTY ', ' Заклятие Абизу ',
#                ' Знакомство родителей ', ' Амстердам ', ' Свободные отношения ', ' Форма голоса (RU SUB) ',
#                ' Чебурашка '}
data_tr=[('R2 S', '2023-02-20T11:10:00.000+0300', 'SQ', 'SQ5FR_WTLR_FTR-2D_S_RU-XX_RU-6_51_2K_ST_20230203_CLB_IOP_VF'), ('R2 S', '2023-02-20T13:00:00.000+0300', 'AmazingMaurice_F', 'AMAZINGMAURICE_WTLR_FTR_F_RU-XX_RU-6_51_4K_IND_20230113_CLB_SMPTE_VF'), ('R3 F 3D', '2023-02-20T12:50:00.000+0300', 'VIP CHEBURASHKA', 'CHEBURASHKA_FTR-5_S-239_RU-XX_RU-06_51_2K_YBW_20221225_PSC_IOP_OV'), ('R4 S', '2023-02-20T14:25:00.000+0300', 'MaybeIDo_F', 'MAYBEIDO_FTR_F_RU-XX_16_51_4K_EXP_20230205_PRG_IOP_VF'), ('R2 S', '2023-02-20T15:10:00.000+0300', 'CHEBURASHKA', 'CHEBURASHKA_FTR-5_S-239_RU-XX_RU-06_51_2K_YBW_20221225_PSC_IOP_OV'), ('R5 S', '2023-02-20T15:20:00.000+0300', 'ASTERIXEMPIRE', 'ASTERIXEMPIRE_FTR-INTER_S-240_RU-XX_BY-12_51_4K_20230210_D24_IOP_VF'), ('R3 F 3D', '2023-02-20T15:30:00.000+0300', 'VIP PiBLastWish', 'PIBLASTWISH_FTR-1_S-240_RU-XX_51_2K_20230111_RED_SMPTE_OV'), ('R4 S', '2023-02-20T16:40:00.000+0300', 'SVO', 'SVO_FTR_S_RU-XX_RU-16_51_2K_20230131_MM_IOP_VF'), ('R2 S', '2023-02-20T17:40:00.000+0300', 'SQ', 'SQ5FR_WTLR_FTR-2D_S_RU-XX_RU-6_51_2K_ST_20230203_CLB_IOP_VF'), ('R3 F 3D', '2023-02-20T18:00:00.000+0300', 'VIP CHEBURASHKA', 'CHEBURASHKA_FTR-5_S-239_RU-XX_RU-06_51_2K_YBW_20221225_PSC_IOP_OV'), ('R4 S', '2023-02-20T19:00:00.000+0300', 'ASTERIXEMPIRE', 'ASTERIXEMPIRE_FTR-INTER_S-240_RU-XX_BY-12_51_4K_20230210_D24_IOP_VF'), ('R5 S', '2023-02-20T17:50:00.000+0300', 'BLUEWATERPEOPL', 'BLUEWATERPEOPL_FTR-1_S_RU-RU_51_2K_20221214_PES_IOP_OV'), ('R2 S', '2023-02-20T19:30:00.000+0300', 'Naughty', 'NAUGHTY_FTR_S_RU-XX_RU_51_2K_NULL_20230210_BMR_IOP_VF'), ('R3 F 3D', '2023-02-20T20:35:00.000+0300', 'VIP_TOPGUNMAVERICK', 'LK_TOPGUNMAVERICK_S'), ('R4 S', '2023-02-20T21:20:00.000+0300', 'MaybeIDo_F', 'MAYBEIDO_FTR_F_RU-XX_16_51_4K_EXP_20230205_PRG_IOP_VF'), ('R5 S', '2023-02-20T21:35:00.000+0300', 'Naughty', 'NAUGHTY_FTR_S_RU-XX_RU_51_2K_NULL_20230210_BMR_IOP_VF'), ('R2 S', '2023-02-20T21:50:00.000+0300', 'TheCommunion', 'THECOMMUNION_FTR_S_RU-XX_18_51_2K_EXP_20230210_PRG_IOP_VF'), ('R2 S', '2023-02-21T11:10:00.000+0300', 'SQ', 'SQ5FR_WTLR_FTR-2D_S_RU-XX_RU-6_51_2K_ST_20230203_CLB_IOP_VF'), ('R2 S', '2023-02-21T13:00:00.000+0300', 'AmazingMaurice_F', 'AMAZINGMAURICE_WTLR_FTR_F_RU-XX_RU-6_51_4K_IND_20230113_CLB_SMPTE_VF'), ('R5 S', '2023-02-21T14:00:00.000+0300', 'CHEBURASHKA', 'CHEBURASHKA_FTR-5_S-239_RU-XX_RU-06_51_2K_YBW_20221225_PSC_IOP_OV'), ('R4 S', '2023-02-21T14:25:00.000+0300', 'MaybeIDo_F', 'MAYBEIDO_FTR_F_RU-XX_16_51_4K_EXP_20230205_PRG_IOP_VF'), ('R2 S', '2023-02-21T15:10:00.000+0300', 'CHEBURASHKA', 'CHEBURASHKA_FTR-5_S-239_RU-XX_RU-06_51_2K_YBW_20221225_PSC_IOP_OV'), ('R3 F 3D', '2023-02-21T15:30:00.000+0300', 'VIP PiBLastWish', 'PIBLASTWISH_FTR-1_S-240_RU-XX_51_2K_20230111_RED_SMPTE_OV'), ('R5 S', '2023-02-21T16:30:00.000+0300', 'ASTERIXEMPIRE', 'ASTERIXEMPIRE_FTR-INTER_S-240_RU-XX_BY-12_51_4K_20230210_D24_IOP_VF'), ('R4 S', '2023-02-21T16:40:00.000+0300', 'SVO', 'SVO_FTR_S_RU-XX_RU-16_51_2K_20230131_MM_IOP_VF'), ('R2 S', '2023-02-21T17:40:00.000+0300', 'SQ', 'SQ5FR_WTLR_FTR-2D_S_RU-XX_RU-6_51_2K_ST_20230203_CLB_IOP_VF'), ('R3 F 3D', '2023-02-21T17:50:00.000+0300', 'VIP CHEBURASHKA', 'CHEBURASHKA_FTR-5_S-239_RU-XX_RU-06_51_2K_YBW_20221225_PSC_IOP_OV'), ('R4 S', '2023-02-21T19:00:00.000+0300', 'ASTERIXEMPIRE', 'ASTERIXEMPIRE_FTR-INTER_S-240_RU-XX_BY-12_51_4K_20230210_D24_IOP_VF'), ('R5 S', '2023-02-21T18:50:00.000+0300', 'TOPGUNMAVERICK', 'LK_TOPGUNMAVERICK_S'), ('R2 S', '2023-02-21T19:30:00.000+0300', 'Naughty', 'NAUGHTY_FTR_S_RU-XX_RU_51_2K_NULL_20230210_BMR_IOP_VF'), ('R4 S', '2023-02-21T21:20:00.000+0300', 'MaybeIDo_F', 'MAYBEIDO_FTR_F_RU-XX_16_51_4K_EXP_20230205_PRG_IOP_VF'), ('R5 S', '2023-02-21T21:35:00.000+0300', 'Naughty', 'NAUGHTY_FTR_S_RU-XX_RU_51_2K_NULL_20230210_BMR_IOP_VF'), ('R2 S', '2023-02-21T21:50:00.000+0300', 'TheCommunion', 'THECOMMUNION_FTR_S_RU-XX_18_51_2K_EXP_20230210_PRG_IOP_VF'), ('R3 F 3D', '2023-02-21T20:20:00.000+0300', '3D BLUEWATERPEOPL', 'BLUEWATERPEOPL_FTR-1-3D-4FL_S_RU-XX_51_2K_20221224_PES_IOP-3D_OV'), ('R2 S', '2023-02-22T11:20:00.000+0300', 'SQ', 'SQ5FR_WTLR_FTR-2D_S_RU-XX_RU-6_51_2K_ST_20230203_CLB_IOP_VF'), ('R2 S', '2023-02-22T13:10:00.000+0300', 'CHEBURASHKA', 'CHEBURASHKA_FTR-5_S-239_RU-XX_RU-06_51_2K_YBW_20221225_PSC_IOP_OV'), ('R3 F 3D', '2023-02-22T13:40:00.000+0300', 'VIP PiBLastWish', 'PIBLASTWISH_FTR-1_S-240_RU-XX_51_2K_20230111_RED_SMPTE_OV'), ('R5 S', '2023-02-22T14:20:00.000+0300', 'ASTERIXEMPIRE', 'ASTERIXEMPIRE_FTR-INTER_S-240_RU-XX_BY-12_51_4K_20230210_D24_IOP_VF'), ('R4 S', '2023-02-22T14:40:00.000+0300', 'MaybeIDo_F', 'MAYBEIDO_FTR_F_RU-XX_16_51_4K_EXP_20230205_PRG_IOP_VF'), ('R2 S', '2023-02-22T15:40:00.000+0300', 'AmazingMaurice_F', 'AMAZINGMAURICE_WTLR_FTR_F_RU-XX_RU-6_51_4K_IND_20230113_CLB_SMPTE_VF'), ('R3 F 3D', '2023-02-22T16:00:00.000+0300', 'VIP_SQ', 'SQ5FR_WTLR_FTR-2D_S_RU-XX_RU-6_51_2K_ST_20230203_CLB_IOP_VF'), ('R5 S', '2023-02-22T16:40:00.000+0300', 'Naughty', 'NAUGHTY_FTR_S_RU-XX_RU_51_2K_NULL_20230210_BMR_IOP_VF'), ('R4 S', '2023-02-22T16:50:00.000+0300', 'SVO', 'SVO_FTR_S_RU-XX_RU-16_51_2K_20230131_MM_IOP_VF'), ('R2 S', '2023-02-22T18:20:00.000+0300', 'RockDog3_F', 'ROCKDOG3_FTR-2D_F_RU-XX_RU-6_51_2K_20230116_D24_IOP_VF'), ('R3 F 3D', '2023-02-22T17:50:00.000+0300', 'VIP CHEBURASHKA', 'CHEBURASHKA_FTR-5_S-239_RU-XX_RU-06_51_2K_YBW_20221225_PSC_IOP_OV'), ('R4 S', '2023-02-22T19:05:00.000+0300', 'ASTERIXEMPIRE', 'ASTERIXEMPIRE_FTR-INTER_S-240_RU-XX_BY-12_51_4K_20230210_D24_IOP_VF'), ('R5 S', '2023-02-22T19:00:00.000+0300', 'TOPGUNMAVERICK', 'LK_TOPGUNMAVERICK_S'), ('R4 S', '2023-02-22T21:30:00.000+0300', 'MaybeIDo_F', 'MAYBEIDO_FTR_F_RU-XX_16_51_4K_EXP_20230205_PRG_IOP_VF'), ('R2 S', '2023-02-22T21:20:00.000+0300', 'Naughty', 'NAUGHTY_FTR_S_RU-XX_RU_51_2K_NULL_20230210_BMR_IOP_VF'), ('R5 S', '2023-02-22T21:40:00.000+0300', 'TheCommunion', 'THECOMMUNION_FTR_S_RU-XX_18_51_2K_EXP_20230210_PRG_IOP_VF'), ('R3 F 3D', '2023-02-22T20:20:00.000+0300', '3D BLUEWATERPEOPL', 'BLUEWATERPEOPL_FTR-1-3D-4FL_S_RU-XX_51_2K_20221224_PES_IOP-3D_OV')]
# data=[('R1 S', '2023-02-14T11:35:00.000+0300', 'CHEBURASHKA', 'CHEBURASHKA_FTR-5_S-239_RU-XX_RU-06_51_2K_YBW_20221225_PSC_IOP_OV'), ('R4 S 3D DA', '2023-02-14T12:10:00.000+0300', 'PiBLastWish', 'PIBLASTWISH_FTR-1_S-240_RU-XX_51_2K_20230111_RED_SMPTE_OV'), ('R3 S', '2023-02-14T12:55:00.000+0300', 'AmazingMaurice_F', 'AMAZINGMAURICE_WTLR_FTR_F_RU-XX_RU-6_51_4K_IND_20230113_CLB_SMPTE_VF'), ('R1 S', '2023-02-14T14:05:00.000+0300', 'PiBLastWish', 'PIBLASTWISH_FTR-1_S-240_RU-XX_51_2K_20230111_RED_SMPTE_OV'), ('R4 S 3D DA', '2023-02-14T14:35:00.000+0300', 'MaybeIDo_F', 'MAYBEIDO_FTR_F_RU-XX_16_51_4K_EXP_20230205_PRG_IOP_VF'), ('R3 S', '2023-02-14T15:00:00.000+0300', 'CHEBURASHKA', 'CHEBURASHKA_FTR-5_S-239_RU-XX_RU-06_51_2K_YBW_20221225_PSC_IOP_OV'), ('R2 S 3D DA', '2023-02-14T13:50:00.000+0300', '3D BLUEWATERPEOPL', 'BLUEWATERPEOPL_FTR-1-3D-4FL_S_RU-XX_51_2K_20221224_PES_IOP-3D_OV'), ('R1 S', '2023-02-14T16:20:00.000+0300', 'LK_LyleLyleCrocodile', 'LK_LYLELYLECROCODILE'), ('R4 S 3D DA', '2023-02-14T16:50:00.000+0300', 'OpFortune', 'OPFORTUNE_FTR_S_RU-XX_51_4K_CIS-18_20221222_D24_IOP_VF'), ('R2 S 3D DA', '2023-02-14T17:35:00.000+0300', '3D AmazingMaurice_F', 'AMAZINGMAURICE_WTLR_FTR-1-3D_F_RU-XX_RU-6_51_2K_20230113_CLB_SMPTE-3D_VF'), ('R3 S', '2023-02-14T17:25:00.000+0300', 'Naughty', 'NAUGHTY_FTR_S_RU-XX_RU_51_2K_NULL_20230210_BMR_IOP_VF'), ('R1 S', '2023-02-14T18:35:00.000+0300', 'CHEBURASHKA', 'CHEBURASHKA_FTR-5_S-239_RU-XX_RU-06_51_2K_YBW_20221225_PSC_IOP_OV'), ('R4 S 3D DA', '2023-02-14T19:15:00.000+0300', 'MaybeIDo_F', 'MAYBEIDO_FTR_F_RU-XX_16_51_4K_EXP_20230205_PRG_IOP_VF'), ('R3 S', '2023-02-14T19:45:00.000+0300', 'AmazingMaurice_F', 'AMAZINGMAURICE_WTLR_FTR_F_RU-XX_RU-6_51_4K_IND_20230113_CLB_SMPTE_VF'), ('R1 S', '2023-02-14T21:05:00.000+0300', 'OpFortune', 'OPFORTUNE_FTR_S_RU-XX_51_4K_CIS-18_20221222_D24_IOP_VF'), ('R2 S 3D DA', '2023-02-14T19:50:00.000+0300', '3D BLUEWATERPEOPL', 'BLUEWATERPEOPL_FTR-1-3D-4FL_S_RU-XX_51_2K_20221224_PES_IOP-3D_OV'), ('R4 S 3D DA', '2023-02-14T21:20:00.000+0300', 'LK_Amsterdam', 'LK_AMSTERDAM'), ('R3 S', '2023-02-14T21:50:00.000+0300', 'Naughty', 'NAUGHTY_FTR_S_RU-XX_RU_51_2K_NULL_20230210_BMR_IOP_VF'), ('R1 S', '2023-02-15T11:35:00.000+0300', 'CHEBURASHKA', 'CHEBURASHKA_FTR-5_S-239_RU-XX_RU-06_51_2K_YBW_20221225_PSC_IOP_OV'), ('R4 S 3D DA', '2023-02-15T12:10:00.000+0300', 'PiBLastWish', 'PIBLASTWISH_FTR-1_S-240_RU-XX_51_2K_20230111_RED_SMPTE_OV'), ('R3 S', '2023-02-15T12:55:00.000+0300', 'AmazingMaurice_F', 'AMAZINGMAURICE_WTLR_FTR_F_RU-XX_RU-6_51_4K_IND_20230113_CLB_SMPTE_VF'), ('R1 S', '2023-02-15T14:05:00.000+0300', 'PiBLastWish', 'PIBLASTWISH_FTR-1_S-240_RU-XX_51_2K_20230111_RED_SMPTE_OV'), ('R4 S 3D DA', '2023-02-15T14:35:00.000+0300', 'MaybeIDo_F', 'MAYBEIDO_FTR_F_RU-XX_16_51_4K_EXP_20230205_PRG_IOP_VF'), ('R3 S', '2023-02-15T15:00:00.000+0300', 'CHEBURASHKA', 'CHEBURASHKA_FTR-5_S-239_RU-XX_RU-06_51_2K_YBW_20221225_PSC_IOP_OV'), ('R2 S 3D DA', '2023-02-15T13:50:00.000+0300', '3D BLUEWATERPEOPL', 'BLUEWATERPEOPL_FTR-1-3D-4FL_S_RU-XX_51_2K_20221224_PES_IOP-3D_OV'), ('R1 S', '2023-02-15T16:20:00.000+0300', 'LK_LyleLyleCrocodile', 'LK_LYLELYLECROCODILE'), ('R4 S 3D DA', '2023-02-15T16:50:00.000+0300', 'OpFortune', 'OPFORTUNE_FTR_S_RU-XX_51_4K_CIS-18_20221222_D24_IOP_VF'), ('R2 S 3D DA', '2023-02-15T17:35:00.000+0300', '3D AmazingMaurice_F', 'AMAZINGMAURICE_WTLR_FTR-1-3D_F_RU-XX_RU-6_51_2K_20230113_CLB_SMPTE-3D_VF'), ('R3 S', '2023-02-15T17:25:00.000+0300', 'Naughty', 'NAUGHTY_FTR_S_RU-XX_RU_51_2K_NULL_20230210_BMR_IOP_VF'), ('R1 S', '2023-02-15T18:35:00.000+0300', 'CHEBURASHKA', 'CHEBURASHKA_FTR-5_S-239_RU-XX_RU-06_51_2K_YBW_20221225_PSC_IOP_OV'), ('R4 S 3D DA', '2023-02-15T19:15:00.000+0300', 'MaybeIDo_F', 'MAYBEIDO_FTR_F_RU-XX_16_51_4K_EXP_20230205_PRG_IOP_VF'), ('R3 S', '2023-02-15T19:40:00.000+0300', 'Naughty', 'NAUGHTY_FTR_S_RU-XX_RU_51_2K_NULL_20230210_BMR_IOP_VF'), ('R1 S', '2023-02-15T21:05:00.000+0300', 'OpFortune', 'OPFORTUNE_FTR_S_RU-XX_51_4K_CIS-18_20221222_D24_IOP_VF'), ('R2 S 3D DA', '2023-02-15T19:50:00.000+0300', '3D BLUEWATERPEOPL', 'BLUEWATERPEOPL_FTR-1-3D-4FL_S_RU-XX_51_2K_20221224_PES_IOP-3D_OV'), ('R4 S 3D DA', '2023-02-15T21:20:00.000+0300', 'LK_Amsterdam', 'LK_AMSTERDAM'), ('R3 S', '2023-02-16T11:25:00.000+0300', 'SQ', 'SQ5FR_WTLR_FTR-2D_S_RU-XX_RU-6_51_2K_ST_20230203_CLB_IOP_VF'), ('R1 S', '2023-02-16T11:10:00.000+0300', 'PiBLastWish', 'PIBLASTWISH_FTR-1_S-240_RU-XX_51_2K_20230111_RED_SMPTE_OV'), ('R4 S 3D DA', '2023-02-16T12:30:00.000+0300', 'CHEBURASHKA', 'CHEBURASHKA_FTR-5_S-239_RU-XX_RU-06_51_2K_YBW_20221225_PSC_IOP_OV'), ('R2 S 3D DA', '2023-02-16T12:50:00.000+0300', 'LK_LyleLyleCrocodile', 'LK_LYLELYLECROCODILE'), ('R3 S', '2023-02-16T13:15:00.000+0300', 'AmazingMaurice_F', 'AMAZINGMAURICE_WTLR_FTR_F_RU-XX_RU-6_51_4K_IND_20230113_CLB_SMPTE_VF'), ('R3 S', '2023-02-16T15:25:00.000+0300', 'AsteriksAndAbeliks', None), ('R1 S', '2023-02-16T13:30:00.000+0300', 'CHEBURASHKA', 'CHEBURASHKA_FTR-5_S-239_RU-XX_RU-06_51_2K_YBW_20221225_PSC_IOP_OV'), ('R2 S 3D DA', '2023-02-16T15:10:00.000+0300', 'SQ', 'SQ5FR_WTLR_FTR-2D_S_RU-XX_RU-6_51_2K_ST_20230203_CLB_IOP_VF'), ('R4 S 3D DA', '2023-02-16T15:00:00.000+0300', 'PiBLastWish', 'PIBLASTWISH_FTR-1_S-240_RU-XX_51_2K_20230111_RED_SMPTE_OV'), ('R1 S', '2023-02-16T16:05:00.000+0300', 'LK_TopGunMaverck', 'LK_TOPGUNMAVERICK_S'), ('R4 S 3D DA', '2023-02-16T17:20:00.000+0300', 'MaybeIDo_F', 'MAYBEIDO_FTR_F_RU-XX_16_51_4K_EXP_20230205_PRG_IOP_VF'), ('R2 S 3D DA', '2023-02-16T17:05:00.000+0300', 'LK_Amsterdam', 'LK_AMSTERDAM'), ('R1 S', '2023-02-16T18:50:00.000+0300', 'CHEBURASHKA', 'CHEBURASHKA_FTR-5_S-239_RU-XX_RU-06_51_2K_YBW_20221225_PSC_IOP_OV'), ('R3 S', '2023-02-16T17:50:00.000+0300', 'BLUEWATERPEOPL', 'BLUEWATERPEOPL_FTR-1_S_RU-RU_51_2K_20221214_PES_IOP_OV'), ('R4 S 3D DA', '2023-02-16T19:30:00.000+0300', 'Naughty', 'NAUGHTY_FTR_S_RU-XX_RU_51_2K_NULL_20230210_BMR_IOP_VF'), ('R3 S', '2023-02-16T21:35:00.000+0300', 'AsteriksAndAbeliks', None), ('R2 S 3D DA', '2023-02-16T19:50:00.000+0300', 'BLUEWATERPEOPL', 'BLUEWATERPEOPL_FTR-1_S_RU-RU_51_2K_20221214_PES_IOP_OV'), ('R1 S', '2023-02-16T21:20:00.000+0300', 'LK_TopGunMaverck', 'LK_TOPGUNMAVERICK_S'), ('R4 S 3D DA', '2023-02-16T21:50:00.000+0300', 'Naughty', 'NAUGHTY_FTR_S_RU-XX_RU_51_2K_NULL_20230210_BMR_IOP_VF'), ('R3 S', '2023-02-17T11:25:00.000+0300', 'SQ', 'SQ5FR_WTLR_FTR-2D_S_RU-XX_RU-6_51_2K_ST_20230203_CLB_IOP_VF'), ('R1 S', '2023-02-17T11:10:00.000+0300', 'PiBLastWish', 'PIBLASTWISH_FTR-1_S-240_RU-XX_51_2K_20230111_RED_SMPTE_OV'), ('R4 S 3D DA', '2023-02-17T12:30:00.000+0300', 'CHEBURASHKA', 'CHEBURASHKA_FTR-5_S-239_RU-XX_RU-06_51_2K_YBW_20221225_PSC_IOP_OV'), ('R2 S 3D DA', '2023-02-17T12:50:00.000+0300', 'LK_LyleLyleCrocodile', 'LK_LYLELYLECROCODILE'), ('R3 S', '2023-02-17T13:15:00.000+0300', 'AmazingMaurice_F', 'AMAZINGMAURICE_WTLR_FTR_F_RU-XX_RU-6_51_4K_IND_20230113_CLB_SMPTE_VF'), ('R3 S', '2023-02-17T15:25:00.000+0300', 'AsteriksAndAbeliks', None), ('R1 S', '2023-02-17T13:30:00.000+0300', 'CHEBURASHKA', 'CHEBURASHKA_FTR-5_S-239_RU-XX_RU-06_51_2K_YBW_20221225_PSC_IOP_OV'), ('R2 S 3D DA', '2023-02-17T15:10:00.000+0300', 'SQ', 'SQ5FR_WTLR_FTR-2D_S_RU-XX_RU-6_51_2K_ST_20230203_CLB_IOP_VF'), ('R4 S 3D DA', '2023-02-17T15:00:00.000+0300', 'PiBLastWish', 'PIBLASTWISH_FTR-1_S-240_RU-XX_51_2K_20230111_RED_SMPTE_OV'), ('R1 S', '2023-02-17T16:05:00.000+0300', 'LK_TopGunMaverck', 'LK_TOPGUNMAVERICK_S'), ('R4 S 3D DA', '2023-02-17T17:20:00.000+0300', 'MaybeIDo_F', 'MAYBEIDO_FTR_F_RU-XX_16_51_4K_EXP_20230205_PRG_IOP_VF'), ('R2 S 3D DA', '2023-02-17T17:05:00.000+0300', 'LK_Amsterdam', 'LK_AMSTERDAM'), ('R1 S', '2023-02-17T18:50:00.000+0300', 'CHEBURASHKA', 'CHEBURASHKA_FTR-5_S-239_RU-XX_RU-06_51_2K_YBW_20221225_PSC_IOP_OV'), ('R3 S', '2023-02-17T17:50:00.000+0300', 'BLUEWATERPEOPL', 'BLUEWATERPEOPL_FTR-1_S_RU-RU_51_2K_20221214_PES_IOP_OV'), ('R4 S 3D DA', '2023-02-17T19:25:00.000+0300', 'Naughty', 'NAUGHTY_FTR_S_RU-XX_RU_51_2K_NULL_20230210_BMR_IOP_VF'), ('R3 S', '2023-02-17T21:35:00.000+0300', 'AsteriksAndAbeliks', None), ('R2 S 3D DA', '2023-02-17T19:50:00.000+0300', 'BLUEWATERPEOPL', 'BLUEWATERPEOPL_FTR-1_S_RU-RU_51_2K_20221214_PES_IOP_OV'), ('R1 S', '2023-02-17T21:20:00.000+0300', 'LK_TopGunMaverck', 'LK_TOPGUNMAVERICK_S'), ('R4 S 3D DA', '2023-02-17T21:50:00.000+0300', 'Naughty', 'NAUGHTY_FTR_S_RU-XX_RU_51_2K_NULL_20230210_BMR_IOP_VF'), ('R3 S', '2023-02-18T11:25:00.000+0300', 'SQ', 'SQ5FR_WTLR_FTR-2D_S_RU-XX_RU-6_51_2K_ST_20230203_CLB_IOP_VF'), ('R1 S', '2023-02-18T11:10:00.000+0300', 'PiBLastWish', 'PIBLASTWISH_FTR-1_S-240_RU-XX_51_2K_20230111_RED_SMPTE_OV'), ('R4 S 3D DA', '2023-02-18T12:30:00.000+0300', 'CHEBURASHKA', 'CHEBURASHKA_FTR-5_S-239_RU-XX_RU-06_51_2K_YBW_20221225_PSC_IOP_OV'), ('R2 S 3D DA', '2023-02-18T12:50:00.000+0300', 'LK_LyleLyleCrocodile', 'LK_LYLELYLECROCODILE'), ('R3 S', '2023-02-18T13:15:00.000+0300', 'AmazingMaurice_F', 'AMAZINGMAURICE_WTLR_FTR_F_RU-XX_RU-6_51_4K_IND_20230113_CLB_SMPTE_VF'), ('R1 S', '2023-02-18T13:25:00.000+0300', 'CHEBURASHKA', 'CHEBURASHKA_FTR-5_S-239_RU-XX_RU-06_51_2K_YBW_20221225_PSC_IOP_OV'), ('R3 S', '2023-02-18T15:25:00.000+0300', 'AsteriksAndAbeliks', None), ('R2 S 3D DA', '2023-02-18T15:10:00.000+0300', 'SQ', 'SQ5FR_WTLR_FTR-2D_S_RU-XX_RU-6_51_2K_ST_20230203_CLB_IOP_VF'), ('R4 S 3D DA', '2023-02-18T15:00:00.000+0300', 'PiBLastWish', 'PIBLASTWISH_FTR-1_S-240_RU-XX_51_2K_20230111_RED_SMPTE_OV'), ('R1 S', '2023-02-18T16:05:00.000+0300', 'LK_TopGunMaverck', 'LK_TOPGUNMAVERICK_S'), ('R4 S 3D DA', '2023-02-18T17:20:00.000+0300', 'MaybeIDo_F', 'MAYBEIDO_FTR_F_RU-XX_16_51_4K_EXP_20230205_PRG_IOP_VF'), ('R2 S 3D DA', '2023-02-18T17:05:00.000+0300', 'LK_Amsterdam', 'LK_AMSTERDAM'), ('R1 S', '2023-02-18T18:50:00.000+0300', 'CHEBURASHKA', 'CHEBURASHKA_FTR-5_S-239_RU-XX_RU-06_51_2K_YBW_20221225_PSC_IOP_OV'), ('R3 S', '2023-02-18T17:50:00.000+0300', 'BLUEWATERPEOPL', 'BLUEWATERPEOPL_FTR-1_S_RU-RU_51_2K_20221214_PES_IOP_OV'), ('R4 S 3D DA', '2023-02-18T19:25:00.000+0300', 'Naughty', 'NAUGHTY_FTR_S_RU-XX_RU_51_2K_NULL_20230210_BMR_IOP_VF'), ('R3 S', '2023-02-18T21:35:00.000+0300', 'AsteriksAndAbeliks', None), ('R2 S 3D DA', '2023-02-18T19:50:00.000+0300', 'BLUEWATERPEOPL', 'BLUEWATERPEOPL_FTR-1_S_RU-RU_51_2K_20221214_PES_IOP_OV'), ('R1 S', '2023-02-18T21:20:00.000+0300', 'LK_TopGunMaverck', 'LK_TOPGUNMAVERICK_S'), ('R4 S 3D DA', '2023-02-18T21:50:00.000+0300', 'Naughty', 'NAUGHTY_FTR_S_RU-XX_RU_51_2K_NULL_20230210_BMR_IOP_VF'), ('R3 S', '2023-02-19T11:25:00.000+0300', 'SQ', 'SQ5FR_WTLR_FTR-2D_S_RU-XX_RU-6_51_2K_ST_20230203_CLB_IOP_VF'), ('R1 S', '2023-02-19T11:10:00.000+0300', 'PiBLastWish', 'PIBLASTWISH_FTR-1_S-240_RU-XX_51_2K_20230111_RED_SMPTE_OV'), ('R4 S 3D DA', '2023-02-19T12:30:00.000+0300', 'CHEBURASHKA', 'CHEBURASHKA_FTR-5_S-239_RU-XX_RU-06_51_2K_YBW_20221225_PSC_IOP_OV'), ('R2 S 3D DA', '2023-02-19T12:50:00.000+0300', 'LK_LyleLyleCrocodile', 'LK_LYLELYLECROCODILE'), ('R3 S', '2023-02-19T13:15:00.000+0300', 'AmazingMaurice_F', 'AMAZINGMAURICE_WTLR_FTR_F_RU-XX_RU-6_51_4K_IND_20230113_CLB_SMPTE_VF'), ('R1 S', '2023-02-19T13:25:00.000+0300', 'CHEBURASHKA', 'CHEBURASHKA_FTR-5_S-239_RU-XX_RU-06_51_2K_YBW_20221225_PSC_IOP_OV'), ('R3 S', '2023-02-19T15:25:00.000+0300', 'AsteriksAndAbeliks', None), ('R2 S 3D DA', '2023-02-19T15:10:00.000+0300', 'SQ', 'SQ5FR_WTLR_FTR-2D_S_RU-XX_RU-6_51_2K_ST_20230203_CLB_IOP_VF'), ('R4 S 3D DA', '2023-02-19T15:00:00.000+0300', 'PiBLastWish', 'PIBLASTWISH_FTR-1_S-240_RU-XX_51_2K_20230111_RED_SMPTE_OV'), ('R1 S', '2023-02-19T16:05:00.000+0300', 'LK_TopGunMaverck', 'LK_TOPGUNMAVERICK_S'), ('R4 S 3D DA', '2023-02-19T17:20:00.000+0300', 'MaybeIDo_F', 'MAYBEIDO_FTR_F_RU-XX_16_51_4K_EXP_20230205_PRG_IOP_VF'), ('R2 S 3D DA', '2023-02-19T17:05:00.000+0300', 'LK_Amsterdam', 'LK_AMSTERDAM'), ('R1 S', '2023-02-19T18:50:00.000+0300', 'CHEBURASHKA', 'CHEBURASHKA_FTR-5_S-239_RU-XX_RU-06_51_2K_YBW_20221225_PSC_IOP_OV'), ('R3 S', '2023-02-19T17:50:00.000+0300', 'BLUEWATERPEOPL', 'BLUEWATERPEOPL_FTR-1_S_RU-RU_51_2K_20221214_PES_IOP_OV'), ('R4 S 3D DA', '2023-02-19T19:25:00.000+0300', 'Naughty', 'NAUGHTY_FTR_S_RU-XX_RU_51_2K_NULL_20230210_BMR_IOP_VF'), ('R3 S', '2023-02-19T21:35:00.000+0300', 'AsteriksAndAbeliks', None), ('R2 S 3D DA', '2023-02-19T19:50:00.000+0300', 'BLUEWATERPEOPL', 'BLUEWATERPEOPL_FTR-1_S_RU-RU_51_2K_20221214_PES_IOP_OV'), ('R1 S', '2023-02-19T21:20:00.000+0300', 'LK_TopGunMaverck', 'LK_TOPGUNMAVERICK_S'), ('R4 S 3D DA', '2023-02-19T21:50:00.000+0300', 'Naughty', 'NAUGHTY_FTR_S_RU-XX_RU_51_2K_NULL_20230210_BMR_IOP_VF')]

# data_dana=[('R6 S', '2023-02-14T10:17:00.000+0300', '+14.02_LK_AfterWeFell', 'LK_AFTERWEFELL'), ('R2 F', '2023-02-14T11:20:00.000+0300', 'AmazingMaurice_F', 'AMAZINGMAURICE_WTLR_FTR_F_RU-XX_RU-6_51_4K_IND_20230113_CLB_SMPTE_VF'), ('R1 S 3D DA', '2023-02-14T11:35:00.000+0300', 'LK_LYLELYLECROCODILE', 'LK_LYLELYLECROCODILE'), ('R3 S SX', '2023-02-14T12:10:00.000+0300', 'PiBLastWish', 'PIBLASTWISH_FTR-1_S-240_RU-XX_51_2K_20230111_RED_SMPTE_OV'), ('R7 S', '2023-02-14T12:00:00.000+0300', 'OpFortune', 'OPFORTUNE_FTR_S_RU-XX_51_4K_CIS-18_20221222_D24_IOP_VF'), ('R5 S 3D', '2023-02-14T11:05:00.000+0300', '3D BlueWaterPeopl', 'BLUEWATERPEOPL_FTR-1-3D-4FL_S_RU-XX_51_2K_20221224_PES_IOP-3D_OV'), ('R2 F', '2023-02-14T13:25:00.000+0300', 'AmazingMaurice_F', 'AMAZINGMAURICE_WTLR_FTR_F_RU-XX_RU-6_51_4K_IND_20230113_CLB_SMPTE_VF'), ('R6 S', '2023-02-14T13:40:00.000+0300', 'MaybeIDo_F', 'MAYBEIDO_FTR_F_RU-XX_16_51_4K_EXP_20230205_PRG_IOP_VF'), ('R1 S 3D DA', '2023-02-14T14:00:00.000+0300', 'CHEBURASHKA', 'CHEBURASHKA_FTR-5_S-239_RU-XX_RU-06_51_2K_YBW_20221225_PSC_IOP_OV'), ('R3 S SX', '2023-02-14T14:30:00.000+0300', 'PiBLastWish', 'PIBLASTWISH_FTR-1_S-240_RU-XX_51_2K_20230111_RED_SMPTE_OV'), ('R4 S', '2023-02-14T14:15:00.000+0300', 'OpFortune', 'OPFORTUNE_FTR_S_RU-XX_51_4K_CIS-18_20221222_D24_IOP_VF'), ('R7 S', '2023-02-14T14:40:00.000+0300', 'SVO', 'SVO_FTR_S_RU-XX_RU-16_51_2K_20230131_MM_IOP_VF'), ('R2 F', '2023-02-14T15:40:00.000+0300', 'MaybeIDo_F', 'MAYBEIDO_FTR_F_RU-XX_16_51_4K_EXP_20230205_PRG_IOP_VF'), ('R6 S', '2023-02-14T15:55:00.000+0300', 'PiBLastWish', 'PIBLASTWISH_FTR-1_S-240_RU-XX_51_2K_20230111_RED_SMPTE_OV'), ('R5 S 3D', '2023-02-14T14:50:00.000+0300', '3D BlueWaterPeopl', 'BLUEWATERPEOPL_FTR-1-3D-4FL_S_RU-XX_51_2K_20221224_PES_IOP-3D_OV'), ('R1 S 3D DA', '2023-02-14T16:30:00.000+0300', 'LK_LYLELYLECROCODILE', 'LK_LYLELYLECROCODILE'), ('R4 S', '2023-02-14T16:50:00.000+0300', 'AloneTogether', 'ALONETOGETHER_FTR_S_RU-XX_16_51_2K_RWV_20230206_PRG_IOP_OV'), ('R7 S', '2023-02-14T17:00:00.000+0300', 'SVO', 'SVO_FTR_S_RU-XX_RU-16_51_2K_20230131_MM_IOP_VF'), ('R3 S SX', '2023-02-14T17:10:00.000+0300', 'CHEBURASHKA', 'CHEBURASHKA_FTR-5_S-239_RU-XX_RU-06_51_2K_YBW_20221225_PSC_IOP_OV'), ('R2 F', '2023-02-14T17:50:00.000+0300', 'OV_Silentvoise_F', 'SILENTVOISE_FTR_F_JA-RU_12_51_2K_IK_20230125_PRG_IOP_OV'), ('R5 S 3D', '2023-02-14T18:35:00.000+0300', '3D AmazingMaurice_F', 'AMAZINGMAURICE_WTLR_FTR-1-3D_F_RU-XX_RU-6_51_2K_20230113_CLB_SMPTE-3D_VF'), ('R1 S 3D DA', '2023-02-14T18:50:00.000+0300', 'Naughty', 'NAUGHTY_FTR_S_RU-XX_RU_51_2K_NULL_20230210_BMR_IOP_VF'), ('R4 S', '2023-02-14T19:05:00.000+0300', 'MaybeIDo_F', 'MAYBEIDO_FTR_F_RU-XX_16_51_4K_EXP_20230205_PRG_IOP_VF'), ('R7 S', '2023-02-14T19:30:00.000+0300', 'Naughty', 'NAUGHTY_FTR_S_RU-XX_RU_51_2K_NULL_20230210_BMR_IOP_VF'), ('R6 S', '2023-02-14T18:10:00.000+0300', 'BlueWaterPeopl', 'BLUEWATERPEOPL_FTR-1_S_RU-RU_51_2K_20221214_PES_IOP_OV'), ('R3 S SX', '2023-02-14T19:40:00.000+0300', 'Naughty', 'NAUGHTY_FTR_S_RU-XX_RU_51_2K_NULL_20230210_BMR_IOP_VF'), ('R2 F', '2023-02-14T20:30:00.000+0300', 'M3GAN', 'M3GAN_FTR-1_S_RU-RU_51_2K_20230127_PES_IOP_OV'), ('R4 S', '2023-02-14T21:10:00.000+0300', 'SVO', 'SVO_FTR_S_RU-XX_RU-16_51_2K_20230131_MM_IOP_VF'), ('R6 S', '2023-02-14T21:55:00.000+0300', 'OFFERING', 'OFFERING_FTR_S_RU-XX_BY-18_51_4K_20230131_D24_IOP_VF'), ('R7 S', '2023-02-14T21:37:00.000+0300', 'OpFortune', 'OPFORTUNE_FTR_S_RU-XX_51_4K_CIS-18_20221222_D24_IOP_VF'), ('R1 S 3D DA', '2023-02-14T21:25:00.000+0300', 'LK_Amsterdam', 'LK_AMSTERDAM'), ('R3 S SX', '2023-02-14T22:05:00.000+0300', 'Naughty', 'NAUGHTY_FTR_S_RU-XX_RU_51_2K_NULL_20230210_BMR_IOP_VF'), ('R5 S 3D', '2023-02-14T20:50:00.000+0300', '3D BlueWaterPeopl', 'BLUEWATERPEOPL_FTR-1-3D-4FL_S_RU-XX_51_2K_20221224_PES_IOP-3D_OV'), ('R2 F', '2023-02-15T11:20:00.000+0300', 'AmazingMaurice_F', 'AMAZINGMAURICE_WTLR_FTR_F_RU-XX_RU-6_51_4K_IND_20230113_CLB_SMPTE_VF'), ('R1 S 3D DA', '2023-02-15T11:35:00.000+0300', 'LK_LYLELYLECROCODILE', 'LK_LYLELYLECROCODILE'), ('R3 S SX', '2023-02-15T12:10:00.000+0300', 'PiBLastWish', 'PIBLASTWISH_FTR-1_S-240_RU-XX_51_2K_20230111_RED_SMPTE_OV'), ('R7 S', '2023-02-15T12:00:00.000+0300', 'OpFortune', 'OPFORTUNE_FTR_S_RU-XX_51_4K_CIS-18_20221222_D24_IOP_VF'), ('R5 S 3D', '2023-02-15T11:05:00.000+0300', '3D BlueWaterPeopl', 'BLUEWATERPEOPL_FTR-1-3D-4FL_S_RU-XX_51_2K_20221224_PES_IOP-3D_OV'), ('R2 F', '2023-02-15T13:25:00.000+0300', 'AmazingMaurice_F', 'AMAZINGMAURICE_WTLR_FTR_F_RU-XX_RU-6_51_4K_IND_20230113_CLB_SMPTE_VF'), ('R6 S', '2023-02-15T13:40:00.000+0300', 'MaybeIDo_F', 'MAYBEIDO_FTR_F_RU-XX_16_51_4K_EXP_20230205_PRG_IOP_VF'), ('R1 S 3D DA', '2023-02-15T14:00:00.000+0300', 'CHEBURASHKA', 'CHEBURASHKA_FTR-5_S-239_RU-XX_RU-06_51_2K_YBW_20221225_PSC_IOP_OV'), ('R3 S SX', '2023-02-15T14:30:00.000+0300', 'PiBLastWish', 'PIBLASTWISH_FTR-1_S-240_RU-XX_51_2K_20230111_RED_SMPTE_OV'), ('R4 S', '2023-02-15T13:00:00.000+0300', 'BlueWaterPeopl', 'BLUEWATERPEOPL_FTR-1_S_RU-RU_51_2K_20221214_PES_IOP_OV'), ('R7 S', '2023-02-15T14:40:00.000+0300', 'SVO', 'SVO_FTR_S_RU-XX_RU-16_51_2K_20230131_MM_IOP_VF'), ('R2 F', '2023-02-15T15:40:00.000+0300', 'MaybeIDo_F', 'MAYBEIDO_FTR_F_RU-XX_16_51_4K_EXP_20230205_PRG_IOP_VF'), ('R6 S', '2023-02-15T15:55:00.000+0300', 'PiBLastWish', 'PIBLASTWISH_FTR-1_S-240_RU-XX_51_2K_20230111_RED_SMPTE_OV'), ('R5 S 3D', '2023-02-15T14:50:00.000+0300', '3D BlueWaterPeopl', 'BLUEWATERPEOPL_FTR-1-3D-4FL_S_RU-XX_51_2K_20221224_PES_IOP-3D_OV'), ('R1 S 3D DA', '2023-02-15T16:30:00.000+0300', 'LK_LYLELYLECROCODILE', 'LK_LYLELYLECROCODILE'), ('R4 S', '2023-02-15T16:50:00.000+0300', 'AloneTogether', 'ALONETOGETHER_FTR_S_RU-XX_16_51_2K_RWV_20230206_PRG_IOP_OV'), ('R7 S', '2023-02-15T17:00:00.000+0300', 'Naughty', 'NAUGHTY_FTR_S_RU-XX_RU_51_2K_NULL_20230210_BMR_IOP_VF'), ('R3 S SX', '2023-02-15T17:10:00.000+0300', 'CHEBURASHKA', 'CHEBURASHKA_FTR-5_S-239_RU-XX_RU-06_51_2K_YBW_20221225_PSC_IOP_OV'), ('R2 F', '2023-02-15T17:50:00.000+0300', 'OV_Silentvoise_F', 'SILENTVOISE_FTR_F_JA-RU_12_51_2K_IK_20230125_PRG_IOP_OV'), ('R5 S 3D', '2023-02-15T18:35:00.000+0300', '3D AmazingMaurice_F', 'AMAZINGMAURICE_WTLR_FTR-1-3D_F_RU-XX_RU-6_51_2K_20230113_CLB_SMPTE-3D_VF'), ('R4 S', '2023-02-15T19:05:00.000+0300', 'MaybeIDo_F', 'MAYBEIDO_FTR_F_RU-XX_16_51_4K_EXP_20230205_PRG_IOP_VF'), ('R1 S 3D DA', '2023-02-15T18:50:00.000+0300', 'CHEBURASHKA', 'CHEBURASHKA_FTR-5_S-239_RU-XX_RU-06_51_2K_YBW_20221225_PSC_IOP_OV'), ('R7 S', '2023-02-15T19:30:00.000+0300', 'Naughty', 'NAUGHTY_FTR_S_RU-XX_RU_51_2K_NULL_20230210_BMR_IOP_VF'), ('R6 S', '2023-02-15T18:10:00.000+0300', 'BlueWaterPeopl', 'BLUEWATERPEOPL_FTR-1_S_RU-RU_51_2K_20221214_PES_IOP_OV'), ('R3 S SX', '2023-02-15T19:40:00.000+0300', 'OpFortune', 'OPFORTUNE_FTR_S_RU-XX_51_4K_CIS-18_20221222_D24_IOP_VF'), ('R2 F', '2023-02-15T20:30:00.000+0300', 'M3GAN', 'M3GAN_FTR-1_S_RU-RU_51_2K_20230127_PES_IOP_OV'), ('R4 S', '2023-02-15T21:10:00.000+0300', 'SVO', 'SVO_FTR_S_RU-XX_RU-16_51_2K_20230131_MM_IOP_VF'), ('R6 S', '2023-02-15T21:55:00.000+0300', 'OFFERING', 'OFFERING_FTR_S_RU-XX_BY-18_51_4K_20230131_D24_IOP_VF'), ('R7 S', '2023-02-15T21:35:00.000+0300', 'OpFortune', 'OPFORTUNE_FTR_S_RU-XX_51_4K_CIS-18_20221222_D24_IOP_VF'), ('R1 S 3D DA', '2023-02-15T21:25:00.000+0300', 'LK_Amsterdam', 'LK_AMSTERDAM'), ('R3 S SX', '2023-02-15T22:05:00.000+0300', 'Naughty', 'NAUGHTY_FTR_S_RU-XX_RU_51_2K_NULL_20230210_BMR_IOP_VF'), ('R5 S 3D', '2023-02-15T20:50:00.000+0300', '3D BlueWaterPeopl', 'BLUEWATERPEOPL_FTR-1-3D-4FL_S_RU-XX_51_2K_20221224_PES_IOP-3D_OV'), ('R3 S SX', '2023-02-16T11:20:00.000+0300', 'SQ', 'SQ5FR_WTLR_FTR-2D_S_RU-XX_RU-6_51_2K_ST_20230203_CLB_IOP_VF'), ('R1 S 3D DA', '2023-02-16T11:05:00.000+0300', 'CHEBURASHKA', 'CHEBURASHKA_FTR-5_S-239_RU-XX_RU-06_51_2K_YBW_20221225_PSC_IOP_OV'), ('R7 S', '2023-02-16T13:15:00.000+0300', 'LK_LegieonSuperHeroes', None), ('R2 F', '2023-02-16T12:40:00.000+0300', 'AmazingMaurice_F', 'AMAZINGMAURICE_WTLR_FTR_F_RU-XX_RU-6_51_4K_IND_20230113_CLB_SMPTE_VF'), ('R3 S SX', '2023-02-16T13:05:00.000+0300', 'PiBLastWish', 'PIBLASTWISH_FTR-1_S-240_RU-XX_51_2K_20230111_RED_SMPTE_OV'), ('R5 S 3D', '2023-02-16T12:05:00.000+0300', '3D BlueWaterPeopl', 'BLUEWATERPEOPL_FTR-1-3D-4FL_S_RU-XX_51_2K_20221224_PES_IOP-3D_OV'), ('R1 S 3D DA', '2023-02-16T13:35:00.000+0300', 'CHEBURASHKA', 'CHEBURASHKA_FTR-5_S-239_RU-XX_RU-06_51_2K_YBW_20221225_PSC_IOP_OV'), ('R6 S', '2023-02-16T14:05:00.000+0300', 'AsteriksAndAbeliks', 'ASTERIXEMPIRE_FTR-INTER_S-240_RU-XX_BY-12_51_4K_20230210_D24_IOP_VF'), ('R2 F', '2023-02-16T14:50:00.000+0300', 'LK_LYLELYLECROCODILE', 'LK_LYLELYLECROCODILE'), ('R3 S SX', '2023-02-16T15:30:00.000+0300', 'SQ', 'SQ5FR_WTLR_FTR-2D_S_RU-XX_RU-6_51_2K_ST_20230203_CLB_IOP_VF'), ('R7 S', '2023-02-16T15:15:00.000+0300', 'SVO', 'SVO_FTR_S_RU-XX_RU-16_51_2K_20230131_MM_IOP_VF'), ('R1 S 3D DA', '2023-02-16T16:05:00.000+0300', 'PiBLastWish', 'PIBLASTWISH_FTR-1_S-240_RU-XX_51_2K_20230111_RED_SMPTE_OV'), ('R2 F', '2023-02-16T17:05:00.000+0300', 'SQ', 'SQ5FR_WTLR_FTR-2D_S_RU-XX_RU-6_51_2K_ST_20230203_CLB_IOP_VF'), ('R6 S', '2023-02-16T16:40:00.000+0300', 'AloneTogether', 'ALONETOGETHER_FTR_S_RU-XX_16_51_2K_RWV_20230206_PRG_IOP_OV'), ('R4 S', '2023-02-16T15:50:00.000+0300', 'Elvis', 'ELVISRHS_FTR-1_S_RU-XX_51_2K_20230120_RED_SMPTE_OV'), ('R3 S SX', '2023-02-16T17:20:00.000+0300', 'AsteriksAndAbeliks', 'ASTERIXEMPIRE_FTR-INTER_S-240_RU-XX_BY-12_51_4K_20230210_D24_IOP_VF'), ('R7 S', '2023-02-16T17:30:00.000+0300', 'Naughty', 'NAUGHTY_FTR_S_RU-XX_RU_51_2K_NULL_20230210_BMR_IOP_VF'), ('R5 S 3D', '2023-02-16T16:20:00.000+0300', '3D BlueWaterPeopl', 'BLUEWATERPEOPL_FTR-1-3D-4FL_S_RU-XX_51_2K_20221224_PES_IOP-3D_OV'), ('R1 S 3D DA', '2023-02-16T18:30:00.000+0300', 'CHEBURASHKA', 'CHEBURASHKA_FTR-5_S-239_RU-XX_RU-06_51_2K_YBW_20221225_PSC_IOP_OV'), ('R6 S', '2023-02-16T18:50:00.000+0300', 'TH_MATS-EK-JULIETTA-i-ROMEO_F', 'MATS-EK-JULIETTA-I-ROMEO_FTR-25_F_IT-RU_51_20210704_IOP_VF'), ('R2 F', '2023-02-16T19:00:00.000+0300', 'AsteriksAndAbeliks', 'ASTERIXEMPIRE_FTR-INTER_S-240_RU-XX_BY-12_51_4K_20230210_D24_IOP_VF'), ('R4 S', '2023-02-16T19:20:00.000+0300', 'MaybeIDo_F', 'MAYBEIDO_FTR_F_RU-XX_16_51_4K_EXP_20230205_PRG_IOP_VF'), ('R3 S SX', '2023-02-16T19:40:00.000+0300', 'Naughty', 'NAUGHTY_FTR_S_RU-XX_RU_51_2K_NULL_20230210_BMR_IOP_VF'), ('R7 S', '2023-02-16T19:55:00.000+0300', 'LK_TopGunMaverck', 'LK_TOPGUNMAVERICK_S'), ('R1 S 3D DA', '2023-02-16T21:00:00.000+0300', 'LK_TopGunMaverck', 'LK_TOPGUNMAVERICK_S'), ('R5 S 3D', '2023-02-16T20:05:00.000+0300', '3D BlueWaterPeopl', 'BLUEWATERPEOPL_FTR-1-3D-4FL_S_RU-XX_51_2K_20221224_PES_IOP-3D_OV'), ('R4 S', '2023-02-16T21:35:00.000+0300', 'Naughty', 'NAUGHTY_FTR_S_RU-XX_RU_51_2K_NULL_20230210_BMR_IOP_VF'), ('R2 F', '2023-02-16T21:20:00.000+0300', 'LK_Amsterdam', 'LK_AMSTERDAM'), ('R3 S SX', '2023-02-16T22:00:00.000+0300', 'TheCommunion', 'THECOMMUNION_FTR_S_RU-XX_16_51_2K_EXP_20230206_PRG_IOP_OV'), ('R6 S', '2023-02-16T21:10:00.000+0300', 'BlueWaterPeopl', 'BLUEWATERPEOPL_FTR-1_S_RU-RU_51_2K_20221214_PES_IOP_OV')]
connect_db = sqlite3.connect('..\data\database.db')
cursor = connect_db.cursor()


# #

def insert_data_tms_triniti_sql(data_parsing_triniti, cur, conn, date=str(datetime.date.today())):
    for show in data_parsing_triniti:
        if date in show[1]:
            if show[0] == 'R1':
                cur.execute(
                    "INSERT INTO TRINITI_1_ROOM_TMS (TH_NAME, ROOM, SHOW_START, SPL_TITLE, CPL_TITLE) VALUES (?, ?, ?, ?, ?)",
                    ("mooon в ТРК Triniti", show[0], show[1], show[2], show[3]))
                conn.commit()
            elif show[0] == 'R2 S':
                cur.execute(
                    "INSERT INTO TRINITI_2_ROOM_TMS (TH_NAME, ROOM, SHOW_START, SPL_TITLE, CPL_TITLE) VALUES (?, ?, ?, ?, ?)",
                    ("mooon в ТРК Triniti", show[0], show[1], show[2], show[3]))
                conn.commit()
            elif show[0] == 'R3 F 3D':
                cur.execute(
                    "INSERT INTO TRINITI_3_ROOM_TMS (TH_NAME, ROOM, SHOW_START, SPL_TITLE, CPL_TITLE) VALUES (?, ?, ?, ?, ?)",
                    ("mooon в ТРК Triniti", show[0], show[1], show[2], show[3]))
                conn.commit()
            elif show[0] == 'R4 S':
                cur.execute(
                    "INSERT INTO TRINITI_4_ROOM_TMS (TH_NAME, ROOM, SHOW_START, SPL_TITLE, CPL_TITLE) VALUES (?, ?, ?, ?, ?)",
                    ("mooon в ТРК Triniti", show[0], show[1], show[2], show[3]))
                conn.commit()
            elif show[0] == 'R5 S':
                cur.execute(
                    "INSERT INTO TRINITI_5_ROOM_TMS (TH_NAME, ROOM, SHOW_START, SPL_TITLE, CPL_TITLE) VALUES (?, ?, ?, ?, ?)",
                    ("mooon в ТРК Triniti", show[0], show[1], show[2], show[3]))
                conn.commit()


# clear_parsing_all_table(cursor,connect_db)
insert_data_tms_triniti_sql(data_tr, cursor, connect_db)
connect_db.close()

#  РАЗОБРАТЬСЯ С ПРЕОБРАЗОВАНИЕМ ТАЙМИНГОВ
# print(str(datetime.date.today()) in data[0][1])
# # print(data[0][1]-datetime.timedelta(min=10))
# a=datetime.datetime.strptime(,'%Y-%m-%dT%H:%M:%S.%f%z')
# print(a+datetime.timedelta(minutes=10))
# '2023-02-14T10:17:00.000+0300'
